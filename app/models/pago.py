from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Pago(Base):
    __tablename__ = "pago"
    __table_args__ = {"schema": "vueladata"}

    id_pago: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_compensacion: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.compensacion.id_compensacion"), unique=True)
    clave_idempotencia: Mapped[str] = mapped_column(String(150), unique=True)
    id_transaccion_externa: Mapped[str | None] = mapped_column(String(150), unique=True, nullable=True)
    estado: Mapped[str] = mapped_column(String(30))
    fecha_solicitud_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_actualizacion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
