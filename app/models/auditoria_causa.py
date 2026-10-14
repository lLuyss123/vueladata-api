from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class AuditoriaCausa(Base):
    __tablename__ = "auditoria_causa"
    __table_args__ = {"schema": "vueladata"}

    id_auditoria: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_incidencia: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.incidencia_vuelo.id_incidencia"), unique=True)
    id_observacion_clima_origen: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("vueladata.observacion_clima.id_observacion_clima"), nullable=True)
    id_observacion_clima_destino: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("vueladata.observacion_clima.id_observacion_clima"), nullable=True)
    motivo: Mapped[str] = mapped_column(String(500))
    estado: Mapped[str] = mapped_column(String(30))
    fecha_creacion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_resolucion_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
