from decimal import Decimal
from sqlalchemy import BigInteger, ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class DetalleReserva(Base):
    __tablename__ = "detalle_reserva"
    __table_args__ = (UniqueConstraint('id_vuelo', 'numero_asiento'), UniqueConstraint('id_itinerario', 'numero_secuencia'), {"schema": "vueladata"})

    id_detalle_reserva: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_itinerario: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.itinerario.id_itinerario"))
    id_vuelo: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.vuelo.id_vuelo"))
    numero_secuencia: Mapped[int] = mapped_column(Integer)
    clase_servicio: Mapped[str] = mapped_column(String(40))
    clase_tarifaria: Mapped[str | None] = mapped_column(String(20), nullable=True)
    monto_tarifa_pagada: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    moneda: Mapped[str] = mapped_column(String(3))
    numero_asiento: Mapped[str | None] = mapped_column(String(10), nullable=True)
    estado_segmento: Mapped[str] = mapped_column(String(30))
