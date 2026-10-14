from pydantic import BaseModel, ConfigDict, Field


class PaisBase(BaseModel):
    nombre: str = Field(..., max_length=100, min_length=1)
    codigo_iso: str = Field(..., max_length=3, min_length=1)


class PaisCreate(PaisBase):
    pass


class PaisUpdate(BaseModel):
    nombre: str | None = Field(default=None, max_length=100, min_length=1)
    codigo_iso: str | None = Field(default=None, max_length=3, min_length=1)


class PaisResponse(PaisBase):
    id_pais: int
    model_config = ConfigDict(from_attributes=True)

