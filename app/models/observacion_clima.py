from datetime import datetime
from decimal import Decimal
from sqlalchemy import BigInteger, DateTime, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ObservacionClima(Base):
    __tablename__ = "observacion_clima"
    __table_args__ = (UniqueConstraint('id_aeropuerto', 'fecha_hora_observacion_utc'), {"schema": "vueladata"})

    id_observacion_clima: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_aeropuerto: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.aeropuerto.id_aeropuerto"))
    fecha_hora_observacion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_hora_recepcion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    visibilidad_km: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    velocidad_viento_kmh: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    direccion_viento_grados: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    temperatura_c: Mapped[Decimal | None] = mapped_column(Numeric(5, 2), nullable=True)
    precipitacion_mm: Mapped[Decimal | None] = mapped_column(Numeric(7, 2), nullable=True)
    codigo_clima: Mapped[str | None] = mapped_column(String(30), nullable=True)
