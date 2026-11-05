from datetime import datetime
from decimal import Decimal
from sqlalchemy import BigInteger, Boolean, DateTime, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from shared.models.base import Base

class PosicionAeronave(Base):
    __tablename__ = "posicion_aeronave"
    __table_args__ = {"schema": "vueladata"}

    id_posicion: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    id_aeronave: Mapped[int] = mapped_column(BigInteger)
    fecha_hora_posicion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_hora_recepcion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    latitud: Mapped[Decimal] = mapped_column(Numeric(8, 5))
    longitud: Mapped[Decimal] = mapped_column(Numeric(8, 5))
    altitud_m: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    velocidad_kmh: Mapped[Decimal | None] = mapped_column(Numeric(8, 2), nullable=True)
    rumbo_grados: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    en_tierra: Mapped[bool] = mapped_column(Boolean)
    id_externo_posicion: Mapped[str] = mapped_column(String(150), unique=True)
