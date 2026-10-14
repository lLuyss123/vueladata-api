from sqlalchemy import BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ReservaPasajero(Base):
    __tablename__ = "reserva_pasajero"
    __table_args__ = (UniqueConstraint('id_reserva', 'id_pasajero'), {"schema": "vueladata"})

    id_reserva_pasajero: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_reserva: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.reserva.id_reserva"))
    id_pasajero: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.pasajero.id_pasajero"))
