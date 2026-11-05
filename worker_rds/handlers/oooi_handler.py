import json
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from shared.models.evento_operacional import EventoOperacional
from shared.models.vuelo import Vuelo
from shared.models.incidencia_vuelo import IncidenciaVuelo
from worker_rds.business_rules import resolver_causa

CODIGOS_VALIDOS = {"OUT", "OFF", "ON", "IN"}

def procesar_evento_oooi(body: bytes | str | dict, db: Session) -> str:
    """
    Procesa un evento OOOI (OUT, OFF, ON, IN) originado por el simulador de vuelos.
    
    Retorna:
      - 'ok': procesado y persistido correctamente.
      - 'duplicado': ya existía en la base de datos (RN-09 idempotencia).
      - 'invalido': estructura malformada o código de evento no reconocido.
    """
    if isinstance(body, (bytes, str)):
        data = json.loads(body)
    else:
        data = body

    # ── 1. Validación estructural básica ──────────────────────────────
    id_externo = data.get("id_externo_evento")
    codigo_evento = data.get("codigo_evento")
    id_vuelo = data.get("id_vuelo")

    if not id_externo or not codigo_evento or codigo_evento not in CODIGOS_VALIDOS or not id_vuelo:
        return "invalido"

    # ── 2. Idempotencia (RN-09) ───────────────────────────────────────
    existente = (
        db.query(EventoOperacional)
        .filter_by(id_externo_evento=str(id_externo))
        .first()
    )
    if existente:
        return "duplicado"

    # ── 3. Detección de caos y validación de calidad (HU-05) ──────────
    fecha_raw = data.get("fecha_hora_evento_utc")
    try:
        fecha_evento = datetime.fromisoformat(str(fecha_raw))
        if fecha_evento.tzinfo is None:
            fecha_evento = fecha_evento.replace(tzinfo=timezone.utc)
    except Exception:
        return "invalido"

    codigo_causa = data.get("codigo_causa_original")
    id_causa, es_imputable, causa_valida = resolver_causa(codigo_causa, db=db)

    # Evaluación de estado de validación (restricción BD: PENDIENTE, VALIDO, RECHAZADO)
    if fecha_evento.year < 2020:
        estado_validacion = "RECHAZADO"
        detalle_validacion = f"Año anómalo detectado: {fecha_evento.year} (Paradoja de tiempo)"
    elif codigo_causa and not causa_valida:
        estado_validacion = "RECHAZADO"
        detalle_validacion = f"Causa no reconocida en catálogo: {codigo_causa}"
    else:
        estado_validacion = "VALIDO"
        detalle_validacion = None

    ahora_utc = datetime.now(timezone.utc)

    # ── 4. Insertar en evento_operacional ─────────────────────────────
    nuevo_evento = EventoOperacional(
        id_vuelo=int(id_vuelo),
        id_estado_vuelo=1,  # Programado / En Progreso
        fecha_hora_evento_utc=fecha_evento,
        fecha_hora_recepcion_utc=ahora_utc,
        codigo_evento=codigo_evento,
        codigo_causa_original=codigo_causa,
        id_externo_evento=str(id_externo),
        estado_validacion=estado_validacion,
        detalle_validacion=detalle_validacion,
        fecha_procesamiento_utc=ahora_utc,
    )
    db.add(nuevo_evento)
    db.flush()  # Para obtener el id_evento si se requiere FK

    # ── 5. Actualizar tiempos reales en vuelo e incidencia ─────────────
    if estado_validacion == "VALIDO":
        vuelo = db.query(Vuelo).filter_by(id_vuelo=int(id_vuelo)).first()
        if vuelo:
            campo_map = {
                "OUT": "salida_real_puerta_utc",
                "OFF": "despegue_real_utc",
                "ON":  "aterrizaje_real_utc",
                "IN":  "llegada_real_puerta_utc",
            }
            campo_a_actualizar = campo_map.get(codigo_evento)
            if campo_a_actualizar:
                setattr(vuelo, campo_a_actualizar, fecha_evento)

            # Si es OUT y tiene retraso significativo con causa, registrar incidencia
            if codigo_evento == "OUT" and id_causa:
                minutos_retraso = 0
                if vuelo.salida_programada_utc:
                    prog = vuelo.salida_programada_utc
                    if prog.tzinfo is None:
                        prog = prog.replace(tzinfo=timezone.utc)
                    minutos_retraso = max(0, int((fecha_evento - prog).total_seconds() / 60))

                if minutos_retraso > 0:
                    incidencia = IncidenciaVuelo(
                        id_vuelo=vuelo.id_vuelo,
                        id_evento_origen=nuevo_evento.id_evento,
                        id_causa=id_causa,
                        tipo="RETRASO",
                        minutos_retraso=minutos_retraso,
                        es_causa_principal=True,
                        requiere_auditoria=False,
                        estado_revision="PENDIENTE",
                        fecha_clasificacion_utc=ahora_utc,
                    )
                    db.add(incidencia)

    db.commit()
    return "ok"
