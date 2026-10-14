from sqlalchemy import BigInteger, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Ciudad(Base):
    __tablename__ = "ciudad"
    __table_args__ = (UniqueConstraint('id_pais', 'nombre'), {"schema": "vueladata"})

    id_ciudad: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_pais: Mapped[int] = mapped_column(BigInteger, ForeignKey("vueladata.pais.id_pais"))
    nombre: Mapped[str] = mapped_column(String(120))
