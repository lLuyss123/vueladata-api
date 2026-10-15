from sqlalchemy.orm import Session
from app.models.causa import Causa

def get_causas(db: Session, skip: int = 0, limit: int = 100) -> list[Causa]:                                                            
    """Obtiene una lista de causas con paginación básica."""                                                                            
    return db.query(Causa).offset(skip).limit(limit).all()                                                                              
                                                                                                                                            
def get_causa_by_id(db: Session, id_causa: int) -> Causa | None:                                                                        
    """Busca una causa por su clave primaria. Devuelve None si no existe."""                                                            
    return db.query(Causa).filter(Causa.id_causa == id_causa).first()        