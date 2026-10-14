from sqlalchemy import BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ConexionItinerario(Base):
    __tablename__ = "conexion_itinerario"
    __table_args__ = (UniqueConstraint('id_detalle_reserva_llegada', 'id_detalle_reserva_salida'), {"schema": "vueladata"})

    id_conexion: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_regla_conexion: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.tiempo_minimo_conexion.id_regla_conexion"))
    id_detalle_reserva_llegada: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.detalle_reserva.id_detalle_reserva"))
    id_detalle_reserva_salida: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.detalle_reserva.id_detalle_reserva"))
