from pydantic import BaseModel, ConfigDict, Field


class CiudadBase(BaseModel):
    id_pais: int = Field(...)
    nombre: str = Field(..., max_length=120, min_length=1)


class CiudadCreate(CiudadBase):
    pass


class CiudadUpdate(BaseModel):
    id_pais: int | None = Field(default=None)
    nombre: str | None = Field(default=None, max_length=120, min_length=1)


class CiudadResponse(CiudadBase):
    id_ciudad: int
    model_config = ConfigDict(from_attributes=True)

