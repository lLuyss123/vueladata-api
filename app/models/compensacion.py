from datetime import datetime
from decimal import Decimal
from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Compensacion(Base):
    __tablename__ = "compensacion"
    __table_args__ = {"schema": "vueladata"}

    id_compensacion: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_detalle_reserva: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.detalle_reserva.id_detalle_reserva"), unique=True)
    id_incidencia: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.incidencia_vuelo.id_incidencia"))
    id_regla_compensacion: Mapped[int] = mapped_column(SmallInteger, ForeignKey("vueladata.regla_compensacion.id_regla_compensacion"))
    minutos_imputables: Mapped[int | None] = mapped_column(Integer, nullable=True)
    monto: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    moneda: Mapped[str] = mapped_column(String(3))
    fecha_calculo_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    estado: Mapped[str] = mapped_column(String(30))
