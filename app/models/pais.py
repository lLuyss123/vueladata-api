from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Pais(Base):
    __tablename__ = "pais"
    __table_args__ = {"schema": "vueladata"}

    id_pais: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    codigo_iso: Mapped[str] = mapped_column(String(3), unique=True)
