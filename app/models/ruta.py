from sqlalchemy import BigInteger, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Ruta(Base):
    __tablename__ = "ruta"
    __table_args__ = (UniqueConstraint('id_aeropuerto_origen', 'id_aeropuerto_destino'), {"schema": "vueladata"})

    id_ruta: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_aeropuerto_origen: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.aeropuerto.id_aeropuerto"))
    id_aeropuerto_destino: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.aeropuerto.id_aeropuerto"))
    duracion_estimada_min: Mapped[int] = mapped_column(Integer)
