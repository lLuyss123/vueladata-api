from datetime import datetime
from decimal import Decimal
from sqlalchemy import BigInteger, DateTime, ForeignKey, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Checkin(Base):
    __tablename__ = "checkin"
    __table_args__ = {"schema": "vueladata"}

    id_checkin: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_detalle_reserva: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.detalle_reserva.id_detalle_reserva"), unique=True)
    fecha_hora_checkin_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    estado_checkin: Mapped[str] = mapped_column(String(30))
    numero_tarjeta_embarque: Mapped[str | None] = mapped_column(String(60), unique=True, nullable=True)
    equipaje_cantidad: Mapped[int] = mapped_column(SmallInteger)
    equipaje_peso: Mapped[Decimal] = mapped_column(Numeric(7, 2))
