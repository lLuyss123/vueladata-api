from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Aerolinea(Base):
    __tablename__ = "aerolinea"
    __table_args__ = {"schema": "vueladata"}

    id_aerolinea: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    codigo_iata: Mapped[str] = mapped_column(String(3), unique=True)
    nombre: Mapped[str] = mapped_column(String(180))
