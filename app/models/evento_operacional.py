from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class EventoOperacional(Base):
    __tablename__ = "evento_operacional"
    __table_args__ = {"schema": "vueladata"}

    id_evento: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_vuelo: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.vuelo.id_vuelo"))
    id_estado_vuelo: Mapped[int] = mapped_column(SmallInteger, ForeignKey("vueladata.estado_vuelo.id_estado_vuelo"))
    fecha_hora_evento_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_hora_recepcion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    codigo_evento: Mapped[str] = mapped_column(String(40))
    codigo_causa_original: Mapped[str | None] = mapped_column(String(50), nullable=True)
    id_externo_evento: Mapped[str] = mapped_column(String(150), unique=True)
    estado_validacion: Mapped[str] = mapped_column(String(20))
    detalle_validacion: Mapped[str | None] = mapped_column(String(500), nullable=True)
    fecha_procesamiento_utc: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
