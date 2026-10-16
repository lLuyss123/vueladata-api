from sqlalchemy.orm import Session
from app.models.causa import Causa
from app.schemas.causa import CausaCreate, CausaUpdate


def get_causas(db: Session, skip: int = 0, limit: int = 100) -> list[Causa]:
    """Obtiene el listado de causas con paginación."""
    return db.query(Causa).offset(skip).limit(limit).all()


def get_causa_by_id(db: Session, id_causa: int) -> Causa | None:
    """Busca una causa por su clave primaria."""
    return db.query(Causa).filter(Causa.id_causa == id_causa).first()


def get_causa_by_codigo(db: Session, codigo: str) -> Causa | None:
    """Busca una causa por su código único."""
    return db.query(Causa).filter(Causa.codigo == codigo).first()


def create_causa(db: Session, causa_in: CausaCreate) -> Causa:
    """Crea y persiste una nueva causa en la base de datos."""
    db_causa = Causa(
        codigo=causa_in.codigo,
        nombre=causa_in.nombre,
        descripcion=causa_in.descripcion,
        es_imputable=causa_in.es_imputable,
    )
    db.add(db_causa)
    db.commit()
    db.refresh(db_causa)
    return db_causa


def update_causa(db: Session, db_causa: Causa, causa_in: CausaUpdate) -> Causa:
    """Actualiza los campos de una causa existente."""
    update_data = causa_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_causa, field, value)
    db.commit()
    db.refresh(db_causa)
    return db_causa


def delete_causa(db: Session, db_causa: Causa) -> None:
    """Elimina una causa de la base de datos."""
    db.delete(db_causa)
    db.commit()