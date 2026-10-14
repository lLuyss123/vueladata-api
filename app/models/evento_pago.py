from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class EventoPago(Base):
    __tablename__ = "evento_pago"
    __table_args__ = {"schema": "vueladata"}

    id_evento_pago: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_pago: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.pago.id_pago"))
    id_externo_evento: Mapped[str] = mapped_column(String(150), unique=True)
    estado_reportado: Mapped[str] = mapped_column(String(30))
    fecha_hora_evento_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    fecha_hora_recepcion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
