from datetime import datetime
from sqlalchemy import BigInteger, Boolean, DateTime, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from shared.models.base import Base

class IncidenciaVuelo(Base):
    __tablename__ = "incidencia_vuelo"
    __table_args__ = {"schema": "vueladata"}

    id_incidencia: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    id_vuelo: Mapped[int] = mapped_column(BigInteger)
    id_evento_origen: Mapped[int] = mapped_column(BigInteger, unique=True)
    id_causa: Mapped[int] = mapped_column(SmallInteger)
    tipo: Mapped[str] = mapped_column(String(20))
    minutos_retraso: Mapped[int | None] = mapped_column(Integer, nullable=True)
    es_causa_principal: Mapped[bool] = mapped_column(Boolean)
    requiere_auditoria: Mapped[bool] = mapped_column(Boolean)
    estado_revision: Mapped[str] = mapped_column(String(30))
    fecha_clasificacion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
