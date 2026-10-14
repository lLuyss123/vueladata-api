from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Reubicacion(Base):
    __tablename__ = "reubicacion"
    __table_args__ = {"schema": "vueladata"}

    id_reubicacion: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_detalle_reserva: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.detalle_reserva.id_detalle_reserva"))
    id_incidencia: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.incidencia_vuelo.id_incidencia"))
    id_vuelo_propuesto: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("vueladata.vuelo.id_vuelo"), nullable=True)
    estado: Mapped[str] = mapped_column(String(30))
    fecha_oferta_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    fecha_respuesta_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
