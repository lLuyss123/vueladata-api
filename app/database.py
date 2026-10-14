# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings   # lo creas en el siguiente paso
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(settings.database_url)          # la "conexión" a PostgreSQL
SessionLocal = sessionmaker(bind=engine)               # fábrica de sesiones

def get_db():
    db = SessionLocal()
    try:
        yield db        # entrega la sesión al endpoint
    finally:
        db.close()      # siempre se cierra, aunque haya error

class Base(DeclarativeBase):
    pass