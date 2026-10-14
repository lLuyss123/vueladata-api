from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class EvaluacionConexion(Base):
    __tablename__ = "evaluacion_conexion"
    __table_args__ = {"schema": "vueladata"}

    id_evaluacion: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_conexion: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.conexion_itinerario.id_conexion"))
    fecha_evaluacion_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    llegada_estimada_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    salida_estimada_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    minutos_disponibles: Mapped[int] = mapped_column(Integer)
    minutos_requeridos: Mapped[int] = mapped_column(Integer)
    estado: Mapped[str] = mapped_column(String(20))
