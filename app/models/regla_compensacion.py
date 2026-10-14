from datetime import datetime
from decimal import Decimal
from sqlalchemy import Boolean, DateTime, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ReglaCompensacion(Base):
    __tablename__ = "regla_compensacion"
    __table_args__ = {"schema": "vueladata"}

    id_regla_compensacion: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    tipo_incidencia: Mapped[str] = mapped_column(String(20))
    minutos_minimos: Mapped[int | None] = mapped_column(Integer, nullable=True)
    minutos_maximos: Mapped[int | None] = mapped_column(Integer, nullable=True)
    aviso_max_horas: Mapped[int | None] = mapped_column(Integer, nullable=True)
    porcentaje: Mapped[Decimal] = mapped_column(Numeric(5, 4))
    requiere_reubicacion: Mapped[bool] = mapped_column(Boolean)
    vigente_desde_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    vigente_hasta_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
