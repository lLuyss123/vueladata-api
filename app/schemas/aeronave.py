from pydantic import BaseModel, ConfigDict, Field


class AeronaveBase(BaseModel):
    id_aerolinea: int = Field(...)
    matricula: str = Field(..., max_length=20, min_length=1)
    modelo: str = Field(..., max_length=100, min_length=1)
    capacidad_pasajeros: int = Field(...)
    estado_operativo: str = Field(..., max_length=30, min_length=1)
    codigo_icao24: str | None = Field(default=None, max_length=6)


class AeronaveCreate(AeronaveBase):
    pass


class AeronaveUpdate(BaseModel):
    id_aerolinea: int | None = Field(default=None)
    matricula: str | None = Field(default=None, max_length=20, min_length=1)
    modelo: str | None = Field(default=None, max_length=100, min_length=1)
    capacidad_pasajeros: int | None = Field(default=None)
    estado_operativo: str | None = Field(default=None, max_length=30, min_length=1)
    codigo_icao24: str | None = Field(default=None, max_length=6)


class AeronaveResponse(AeronaveBase):
    id_aeronave: int
    model_config = ConfigDict(from_attributes=True)

