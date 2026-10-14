from sqlalchemy import String, Boolean, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Causa(Base):
    __tablename__ = "causa"
    __table_args__ = {"schema": "vueladata"}   # ¡el schema del script!

    id_causa: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    codigo: Mapped[str] = mapped_column(String(40), unique=True)
    nombre: Mapped[str] = mapped_column(String(120))
    descripcion: Mapped[str | None] = mapped_column(String(500))
    es_imputable: Mapped[bool] = mapped_column(Boolean)