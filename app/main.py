from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.causa import Causa


app = FastAPI(
    title="API VuelaData",
    description="Compensation Payments API",
    version="1.0.0",
)

# endpoint temporal para verificar la db
@app.get("/debug/causas")
def debug_causas(db: Session = Depends(get_db)):
    return [c.codigo for c in db.query(Causa).all()]

@app.get("/health")
def health():
    # Solo confirma que la API está viva (no toca la BD)
    return {"status": "ok"}


@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    # FastAPI inyecta la sesión de la BD gracias a Depends(get_db)
    try:
        db.execute(text("SELECT 1"))  # si la BD está caída, falla aquí
        return {"status": "ok", "database": "online"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="No se pudo conectar con la base de datos",
        )