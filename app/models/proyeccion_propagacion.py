from datetime import datetime
from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ProyeccionPropagacion(Base):
    __tablename__ = "proyeccion_propagacion"
    __table_args__ = {"schema": "vueladata"}

    id_proyeccion: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_vuelo_origen: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.vuelo.id_vuelo"))
    id_vuelo_afectado: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.vuelo.id_vuelo"))
    id_regla_rotacion: Mapped[int] = mapped_column(SmallInteger, ForeignKey("vueladata.regla_rotacion.id_regla_rotacion"))
    retraso_origen_min: Mapped[int] = mapped_column(Integer)
    retraso_proyectado_min: Mapped[int] = mapped_column(Integer)
    fecha_calculo_utc: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    estado: Mapped[str] = mapped_column(String(30))
