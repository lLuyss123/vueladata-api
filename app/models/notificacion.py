from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Notificacion(Base):
    __tablename__ = "notificacion"
    __table_args__ = {"schema": "vueladata"}

    id_notificacion: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_detalle_reserva: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.detalle_reserva.id_detalle_reserva"))
    id_evaluacion_conexion: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("vueladata.evaluacion_conexion.id_evaluacion"), nullable=True)
    id_compensacion: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("vueladata.compensacion.id_compensacion"), nullable=True)
    tipo: Mapped[str] = mapped_column(String(30))
    canal: Mapped[str] = mapped_column(String(20))
    estado_envio: Mapped[str] = mapped_column(String(30))
    fecha_programada_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_envio_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
