from fastapi import APIRouter, Depends, HTTPException, status                                                                           
from sqlalchemy.orm import Session                                                                                                      
                                                                                                                                        
from app.database import get_db                                                                                                         
from app.schemas.causa import CausaResponse                                                                                             
import app.crud.causa as crud_causa                                                                                                     
                                                                                                                                        
router = APIRouter(                                                                                                                     
    prefix="/causas",                                                                                                                   
    tags=["Causas"],  # Agrupa los endpoints ordenadamente en Swagger                                                                   
)                                                                                                                                       
                                                                                                                                        
# --- Endpoint 1: Listar todas las causas ---                                                                                           
@router.get(                                                                                                                            
    "/",                                                                                                                                
    response_model=list[CausaResponse],                                                                                                 
    status_code=status.HTTP_200_OK,                                                                                                     
    summary="Listar todas las causas",                                                                                                  
    description="Devuelve el catálogo de causas operacionales con paginación.",                                                         
)                                                                                                                                       
def read_causas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):                                                        
    causas = crud_causa.get_causas(db, skip=skip, limit=limit)                                                                          
    return causas  # FastAPI lo convierte automáticamente al schema CausaResponse gracias a from_attributes=True                        
                                                                                                                                        
# --- Endpoint 2: Buscar una causa por ID (con manejo de 404) ---                                                                       
@router.get(                                                                                                                            
    "/{id_causa}",                                                                                                                      
    response_model=CausaResponse,                                                                                                       
    status_code=status.HTTP_200_OK,                                                                                                     
    summary="Obtener una causa por ID",                                                                                                 
)                                                                                                                                       
def read_causa(id_causa: int, db: Session = Depends(get_db)):                                                                           
    causa = crud_causa.get_causa_by_id(db, id_causa=id_causa)                                                                           
    if causa is None:                                                                                                                   
        # Criterio 2 de HU-05: Si no existe, devolver código HTTP apropiado y mensaje claro                                             
        raise HTTPException(                                                                                                            
            status_code=status.HTTP_404_NOT_FOUND,                                                                                      
            detail=f"Causa con id {id_causa} no fue encontrada",                                                                        
        )                                                                                                                               
    return causa                           