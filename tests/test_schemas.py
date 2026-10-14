import pytest
from pydantic import ValidationError

from app.models.causa import Causa
from app.schemas.causa import CausaCreate, CausaResponse, CausaUpdate


def test_causa_create_valid():
    """Valida que un esquema CausaCreate con datos válidos se cree correctamente."""
    data = {
        "codigo": "TECNICA",
        "nombre": "Falla técnica de mantenimiento",
        "descripcion": "Problemas de motor reportados en rampa",
        "es_imputable": True,
    }
    causa = CausaCreate(**data)
    assert causa.codigo == "TECNICA"
    assert causa.nombre == "Falla técnica de mantenimiento"
    assert causa.descripcion == "Problemas de motor reportados en rampa"
    assert causa.es_imputable is True


def test_causa_create_valid_without_description():
    """Valida que descripcion sea opcional y por defecto sea None."""
    data = {
        "codigo": "CLIMA",
        "nombre": "Condiciones meteorológicas adversas",
        "es_imputable": False,
    }
    causa = CausaCreate(**data)
    assert causa.codigo == "CLIMA"
    assert causa.descripcion is None
    assert causa.es_imputable is False


def test_causa_create_missing_required_fields():
    """Valida que Pydantic rechace la creación si falta un campo obligatorio."""
    # Falta 'codigo' y 'es_imputable'
    with pytest.raises(ValidationError) as exc_info:
        CausaCreate(nombre="Incompleta")
    errors = exc_info.value.errors()
    missing_fields = {e["loc"][0] for e in errors}
    assert "codigo" in missing_fields
    assert "es_imputable" in missing_fields


def test_causa_create_empty_strings_rejected():
    """Valida que cadenas vacías sean rechazadas según min_length=1."""
    with pytest.raises(ValidationError):
        CausaCreate(
            codigo="",
            nombre="Nombre válido",
            es_imputable=True,
        )


def test_causa_create_max_length_exceeded():
    """Valida que se rechacen cadenas que superen la longitud máxima permitida por la base de datos."""
    # codigo soporta máximo 40 caracteres
    with pytest.raises(ValidationError):
        CausaCreate(
            codigo="A" * 41,
            nombre="Nombre válido",
            es_imputable=True,
        )

    # nombre soporta máximo 120 caracteres
    with pytest.raises(ValidationError):
        CausaCreate(
            codigo="CODIGO_VALIDO",
            nombre="A" * 121,
            es_imputable=True,
        )


def test_causa_response_from_orm():
    """Valida que CausaResponse pueda leer y serializar directamente un objeto ORM de SQLAlchemy."""
    orm_causa = Causa(
        id_causa=1,
        codigo="ATC",
        nombre="Control de Tráfico Aéreo",
        descripcion="Instrucciones de torre",
        es_imputable=False,
    )

    response = CausaResponse.model_validate(orm_causa)
    assert response.id_causa == 1
    assert response.codigo == "ATC"
    assert response.nombre == "Control de Tráfico Aéreo"
    assert response.es_imputable is False
