from pydantic import BaseModel, ConfigDict, Field


class AerolineaBase(BaseModel):
    codigo_iata: str = Field(..., max_length=3, min_length=1)
    nombre: str = Field(..., max_length=180, min_length=1)


class AerolineaCreate(AerolineaBase):
    pass


class AerolineaUpdate(BaseModel):
    codigo_iata: str | None = Field(default=None, max_length=3, min_length=1)
    nombre: str | None = Field(default=None, max_length=180, min_length=1)


class AerolineaResponse(AerolineaBase):
    id_aerolinea: int
    model_config = ConfigDict(from_attributes=True)

