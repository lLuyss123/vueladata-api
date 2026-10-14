from datetime import datetime
from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Reserva(Base):
    __tablename__ = "reserva"
    __table_args__ = {"schema": "vueladata"}

    id_reserva: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    codigo_reserva: Mapped[str] = mapped_column(String(20), unique=True)
    fecha_reserva_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    estado_reserva: Mapped[str] = mapped_column(String(30))
    fecha_actualizacion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
