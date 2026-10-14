from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class EstadoVuelo(Base):
    __tablename__ = "estado_vuelo"
    __table_args__ = {"schema": "vueladata"}

    id_estado_vuelo: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    codigo: Mapped[str] = mapped_column(String(40), unique=True)
    nombre: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[str | None] = mapped_column(String(300), nullable=True)
