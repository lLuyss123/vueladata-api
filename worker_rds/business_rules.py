import hashlib
from decimal import Decimal
from typing import Optional
from sqlalchemy.orm import Session
from shared.models.causa import Causa

# Catálogo conocido de causas válidas
CAUSAS_CONOCIDAS = {
    "TECNICA": {"id_causa": 1, "es_imputable": True, "nombre": "Falla técnica de aeronave"},
    "TRIPULACION": {"id_causa": 2, "es_imputable": True, "nombre": "Falta o descanso de tripulación"},
    "OPERACIONAL": {"id_causa": 3, "es_imputable": True, "nombre": "Problemas operacionales internos"},
    "CLIMA": {"id_causa": 4, "es_imputable": False, "nombre": "Condiciones meteorológicas adversas"},
}

def resolver_causa(codigo_causa: Optional[str], db: Optional[Session] = None) -> tuple[Optional[int], bool, bool]:
    """
    RN-03: Clasifica la causa del evento.
    Retorna: (id_causa, es_imputable, es_valida)
    """
    if not codigo_causa:
        return None, False, True

    codigo_upper = codigo_causa.strip().upper()

    # Si es un código de error de caos como ERROR_99
    if codigo_upper.startswith("ERROR") or codigo_upper == "INVALIDA":
        return None, False, False

    # Intentar buscar en la base de datos si la sesión está disponible
    if db is not None:
        try:
            causa_db = db.query(Causa).filter_by(codigo=codigo_upper).first()
            if causa_db:
                return causa_db.id_causa, bool(causa_db.es_imputable), True
        except Exception:
            pass  # Fallback al catálogo en memoria

    # Búsqueda en catálogo base conocido
    if codigo_upper in CAUSAS_CONOCIDAS:
        c = CAUSAS_CONOCIDAS[codigo_upper]
        return c["id_causa"], c["es_imputable"], True

    return None, False, False

def evaluar_condiciones_adversas(
    velocidad_viento_kmh: Optional[float | Decimal] = None,
    visibilidad_km: Optional[float | Decimal] = None,
    codigo_clima: Optional[str] = None
) -> bool:
    """
    RN-04: Evalúa si existen condiciones climáticas adversas en la zona.
    Condiciones:
    - Viento superior a 50 km/h
    - Visibilidad menor a 1.0 km
    - Códigos climáticos extremos (TORMENTA, HURACAN, NIEBLA_DENSA)
    """
    if velocidad_viento_kmh is not None and float(velocidad_viento_kmh) > 50.0:
        return True
    if visibilidad_km is not None and float(visibilidad_km) < 1.0:
        return True
    if codigo_clima:
        clima_upper = codigo_clima.upper()
        if any(w in clima_upper for w in ("TORMENTA", "HURACAN", "STORM", "FOG", "NIEBLA")):
            return True
    return False

def calcular_porcentaje_compensacion(minutos_retraso: int, es_imputable: bool) -> Decimal:
    """
    RN-05: Calcula el porcentaje de compensación según minutos de retraso e imputabilidad.
    """
    if not es_imputable or minutos_retraso < 120:
        return Decimal("0.00")
    elif 120 <= minutos_retraso < 180:
        return Decimal("25.00")
    elif 180 <= minutos_retraso < 240:
        return Decimal("50.00")
    else:  # >= 240 min (4 horas o más)
        return Decimal("100.00")

def generar_clave_idempotencia(id_vuelo: int, id_pasajero: int, id_evento: int) -> str:
    """
    RN-09: Genera una clave hash única e idempotente para evitar compensaciones duplicadas.
    """
    raw = f"{id_vuelo}:{id_pasajero}:{id_evento}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
