from sqlalchemy import BigInteger, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Aeronave(Base):
    __tablename__ = "aeronave"
    __table_args__ = {"schema": "vueladata"}

    id_aeronave: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_aerolinea: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.aerolinea.id_aerolinea"))
    matricula: Mapped[str] = mapped_column(String(20), unique=True)
    modelo: Mapped[str] = mapped_column(String(100))
    capacidad_pasajeros: Mapped[int] = mapped_column(Integer)
    estado_operativo: Mapped[str] = mapped_column(String(30))
    codigo_icao24: Mapped[str | None] = mapped_column(String(6), unique=True, nullable=True)
