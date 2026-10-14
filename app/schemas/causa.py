from pydantic import BaseModel, ConfigDict, Field


class CausaBase(BaseModel):
    codigo: str = Field(
        ...,
        min_length=1,
        max_length=40,
        description="Código único de la causa (ej. TECNICA, CLIMA)",
    )
    nombre: str = Field(
        ...,
        min_length=1,
        max_length=120,
        description="Nombre legible de la causa",
    )
    descripcion: str | None = Field(
        default=None,
        max_length=500,
        description="Descripción o justificación detallada de la causa",
    )
    es_imputable: bool = Field(
        ...,
        description="Indica si la responsabilidad es de la aerolínea (RN-03)",
    )


class CausaCreate(CausaBase):
    """Esquema para crear una nueva causa.
    No incluye id_causa porque la base de datos lo genera automáticamente.
    """
    pass


class CausaUpdate(BaseModel):
    """Esquema para actualizar una causa existente.
    Todos los campos son opcionales para permitir actualizaciones parciales.
    """
    codigo: str | None = Field(default=None, min_length=1, max_length=40)
    nombre: str | None = Field(default=None, min_length=1, max_length=120)
    descripcion: str | None = Field(default=None, max_length=500)
    es_imputable: bool | None = Field(default=None)


class CausaResponse(CausaBase):
    """Esquema que devuelve la API.
    Incluye la clave primaria id_causa y la configuración para leer objetos ORM.
    """
    id_causa: int

    model_config = ConfigDict(from_attributes=True)
