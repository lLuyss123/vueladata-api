from pydantic import BaseModel, ConfigDict, Field


class EstadoVueloBase(BaseModel):
    codigo: str = Field(..., max_length=40, min_length=1)
    nombre: str = Field(..., max_length=100, min_length=1)
    descripcion: str | None = Field(default=None, max_length=300)


class EstadoVueloCreate(EstadoVueloBase):
    pass


class EstadoVueloUpdate(BaseModel):
    codigo: str | None = Field(default=None, max_length=40, min_length=1)
    nombre: str | None = Field(default=None, max_length=100, min_length=1)
    descripcion: str | None = Field(default=None, max_length=300)


class EstadoVueloResponse(EstadoVueloBase):
    id_estado_vuelo: int
    model_config = ConfigDict(from_attributes=True)

