from sqlalchemy.orm import Session
from app.models.regla_compensacion import ReglaCompensacion
from app.schemas.regla_compensacion import ReglaCompensacionCreate, ReglaCompensacionUpdate


def get_reglas_compensacion(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    tipo_incidencia: str | None = None,
) -> list[ReglaCompensacion]:
    """Obtiene reglas de compensación, opcionalmente filtradas por tipo de incidencia."""
    query = db.query(ReglaCompensacion)
    if tipo_incidencia:
        query = query.filter(ReglaCompensacion.tipo_incidencia == tipo_incidencia)
    return query.offset(skip).limit(limit).all()


def get_regla_compensacion_by_id(db: Session, id_regla: int) -> ReglaCompensacion | None:
    """Busca una regla de compensación por su ID."""
    return db.query(ReglaCompensacion).filter(ReglaCompensacion.id_regla_compensacion == id_regla).first()


def create_regla_compensacion(db: Session, regla_in: ReglaCompensacionCreate) -> ReglaCompensacion:
    """Crea una nueva regla de compensación."""
    db_regla = ReglaCompensacion(**regla_in.model_dump())
    db.add(db_regla)
    db.commit()
    db.refresh(db_regla)
    return db_regla


def update_regla_compensacion(
    db: Session, db_regla: ReglaCompensacion, regla_in: ReglaCompensacionUpdate
) -> ReglaCompensacion:
    """Actualiza una regla de compensación existente."""
    update_data = regla_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_regla, field, value)
    db.commit()
    db.refresh(db_regla)
    return db_regla


def delete_regla_compensacion(db: Session, db_regla: ReglaCompensacion) -> None:
    """Elimina una regla de compensación."""
    db.delete(db_regla)
    db.commit()
