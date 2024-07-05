from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..crud import crud

from ..schemas import location
from ..database import database

router = APIRouter(
    prefix="/locations",
    tags=["Ubicaciones"]
)

@router.post("/", response_model=location.Location, status_code=status.HTTP_201_CREATED, summary="Crear una nueva ubicación")
def create_location(location: location.LocationCreate, db: Session = Depends(database.get_db)):
    """
    Crea una nueva ubicación.

    - **name**: nombre de la ubicación
    - **description**: descripción de la ubicación
    - **latitude**: latitud de la ubicación
    - **longitude**: longitud de la ubicación
    - **category_id**: ID de la categoría a la que pertenece la ubicación
    """
    db_location = crud.create_location(db=db, location=location)
    if db_location is None:
        raise HTTPException(status_code=400, detail="Error al crear la ubicación.")
    return db_location

@router.get("/", response_model=list[location.Location], summary="Listar todas las ubicaciones")
def read_locations(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    """
    Obtiene una lista de todas las ubicaciones.

    - **skip**: número de registros a saltar
    - **limit**: número máximo de registros a devolver
    """
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations

@router.get("/{location_id}", response_model=location.Location, summary="Obtener una ubicación por ID", description="Endpoint para obtener una ubicación específica por su ID.")
def read_location(location_id: int, db: Session = Depends(database.get_db)):
    db_location = crud.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada.")
    return db_location
