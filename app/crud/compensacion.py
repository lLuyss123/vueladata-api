from sqlalchemy.orm import Session
from app.models.compensacion import Compensacion
from app.schemas.compensacion import CompensacionCreate, CompensacionUpdate


def get_compensaciones(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    estado: str | None = None,
    id_detalle_reserva: int | None = None,
) -> list[Compensacion]:
    """Obtiene la lista de compensaciones con filtros opcionales."""
    query = db.query(Compensacion)
    if estado:
        query = query.filter(Compensacion.estado == estado)
    if id_detalle_reserva:
        query = query.filter(Compensacion.id_detalle_reserva == id_detalle_reserva)
    return query.offset(skip).limit(limit).all()


def get_compensacion_by_id(db: Session, id_compensacion: int) -> Compensacion | None:
    """Busca una compensación por su clave primaria."""
    return db.query(Compensacion).filter(Compensacion.id_compensacion == id_compensacion).first()


def get_compensacion_by_detalle_reserva(db: Session, id_detalle_reserva: int) -> Compensacion | None:
    """Busca si un segmento de reserva ya tiene compensación asignada (RN-09)."""
    return db.query(Compensacion).filter(Compensacion.id_detalle_reserva == id_detalle_reserva).first()


def create_compensacion(db: Session, comp_in: CompensacionCreate) -> Compensacion:
    """Registra una nueva compensación económica."""
    db_comp = Compensacion(**comp_in.model_dump())
    db.add(db_comp)
    db.commit()
    db.refresh(db_comp)
    return db_comp


def update_compensacion(
    db: Session, db_comp: Compensacion, comp_in: CompensacionUpdate
) -> Compensacion:
    """Actualiza una compensación existente."""
    update_data = comp_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_comp, field, value)
    db.commit()
    db.refresh(db_comp)
    return db_comp


def delete_compensacion(db: Session, db_comp: Compensacion) -> None:
    """Elimina un registro de compensación."""
    db.delete(db_comp)
    db.commit()
