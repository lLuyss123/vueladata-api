from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.pago import Pago
from app.schemas.pago import PagoCreate, PagoUpdate


def get_pagos(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    estado: str | None = None,
) -> list[Pago]:
    """Obtiene el listado de solicitudes de pago con filtros opcionales."""
    query = db.query(Pago)
    if estado:
        query = query.filter(Pago.estado == estado)
    return query.offset(skip).limit(limit).all()


def get_pago_by_id(db: Session, id_pago: int) -> Pago | None:
    """Busca un pago por su clave primaria."""
    return db.query(Pago).filter(Pago.id_pago == id_pago).first()


def get_pago_by_clave_idempotencia(db: Session, clave_idempotencia: str) -> Pago | None:
    """Busca un pago por su clave de idempotencia."""
    return db.query(Pago).filter(Pago.clave_idempotencia == clave_idempotencia).first()


def get_pago_by_compensacion(db: Session, id_compensacion: int) -> Pago | None:
    """Busca si una compensación ya tiene un pago asociado."""
    return db.query(Pago).filter(Pago.id_compensacion == id_compensacion).first()


def create_pago(db: Session, pago_in: PagoCreate) -> Pago:
    """Crea una nueva solicitud de pago hacia la pasarela F7."""
    db_pago = Pago(**pago_in.model_dump())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago


def update_pago(db: Session, db_pago: Pago, pago_in: PagoUpdate) -> Pago:
    """Actualiza el estado o transacción de un pago existente."""
    update_data = pago_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_pago, field, value)
    db_pago.fecha_actualizacion_utc = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_pago)
    return db_pago


def delete_pago(db: Session, db_pago: Pago) -> None:
    """Elimina un registro de pago."""
    db.delete(db_pago)
    db.commit()
