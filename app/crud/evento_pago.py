from sqlalchemy.orm import Session
from app.models.evento_pago import EventoPago
from app.schemas.evento_pago import EventoPagoCreate


def get_eventos_pago(
    db: Session,
    id_pago: int | None = None,
    skip: int = 0,
    limit: int = 100,
) -> list[EventoPago]:
    """Obtiene el historial de eventos asíncronos de pago recibidos."""
    query = db.query(EventoPago)
    if id_pago:
        query = query.filter(EventoPago.id_pago == id_pago)
    return query.order_by(EventoPago.fecha_hora_recepcion_utc.desc()).offset(skip).limit(limit).all()


def get_evento_pago_by_id(db: Session, id_evento_pago: int) -> EventoPago | None:
    """Busca un evento de pago por su clave primaria."""
    return db.query(EventoPago).filter(EventoPago.id_evento_pago == id_evento_pago).first()


def get_evento_pago_by_externo(db: Session, id_externo_evento: str) -> EventoPago | None:
    """Busca un evento por su clave externa idempotente."""
    return db.query(EventoPago).filter(EventoPago.id_externo_evento == id_externo_evento).first()


def create_evento_pago(db: Session, evento_in: EventoPagoCreate) -> EventoPago:
    """Registra un evento de pago devuelto por la pasarela F7."""
    db_evento = EventoPago(**evento_in.model_dump())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento
