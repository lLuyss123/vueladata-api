from datetime import datetime
from sqlalchemy import DateTime, Integer, SmallInteger, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ReglaRotacion(Base):
    __tablename__ = "regla_rotacion"
    __table_args__ = (UniqueConstraint('tipo_vuelo', 'vigente_desde_utc'), {"schema": "vueladata"})

    id_regla_rotacion: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    tipo_vuelo: Mapped[str] = mapped_column(String(20))
    minutos_minimos: Mapped[int] = mapped_column(Integer)
    vigente_desde_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    vigente_hasta_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
