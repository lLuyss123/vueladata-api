from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.causa import Causa
from app.routers.causa import router as causas_router


app = FastAPI(
    title="API VuelaData",
    description="Compensation Payments API",
    version="1.0.0",
)


app.include_router(causas_router) 

@app.get("/health")
def health():
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