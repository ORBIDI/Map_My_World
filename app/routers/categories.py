from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from ..crud import crud

from ..schemas import category
from ..database import database

router = APIRouter(
    prefix="/categories",
    tags=["Categorías"]
)

@router.post("/", response_model=category.Category, status_code=status.HTTP_201_CREATED, summary="Crear una nueva categoría")
def create_category(category: category.CategoryCreate, db: Session = Depends(database.get_db)):
    """
    Crea una nueva categoría.

    - **name**: nombre de la categoría
    - **description**: descripción de la categoría
    """    
    db_category = crud.create_category(db=db, category=category)
    if db_category is None:        
        raise HTTPException(status_code=400, detail="Error al crear la categoría.")
    return db_category

@router.get("/", response_model=list[category.Category], summary="Listar todas las categorías")
def get_categories(skip: int = Query(0, description="Número de registros a omitir"),
                   limit: int = Query(10, description="Número máximo de registros a devolver"),
                   db: Session = Depends(database.get_db)):
    """
    Obtiene una lista de todas las categorías.

    - **skip**: número de registros a saltar
    - **limit**: número máximo de registros a devolver
    """
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/{category_id}", response_model=category.Category, summary="Obtener una categoría por ID", description="Endpoint para obtener una categoría específica por su ID.")
def get_category(category_id: int, db: Session = Depends(database.get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada.")
    return db_category
