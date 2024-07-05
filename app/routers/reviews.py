from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..crud import crud

from ..schemas import reviewed
from ..database import database

router = APIRouter(
    prefix="/reviews",
    tags=["Revisiones"]
)

@router.post("/", response_model=reviewed.LocationCategoryReviewed, status_code=status.HTTP_201_CREATED, summary="Crear una revisión de ubicación-categoría")
def create_review(review: reviewed.LocationCategoryReviewedCreate, db: Session = Depends(database.get_db)):
    """
    Crea una nueva revisión de ubicación-categoría.

    - **location_id**: ID de la ubicación
    - **category_id**: ID de la categoría
    - **last_reviewed**: fecha de la última revisión
    """
    db_review = crud.get_location_category_reviewed(db, location_id=review.location_id, category_id=review.category_id)
    if db_review:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Review already exists")
    return crud.create_location_category_reviewed(db=db, review=review)

@router.put("/", response_model=reviewed.LocationCategoryReviewedUpdate, summary="Actualizar una revisión de ubicación-categoría")
def update_review(review: reviewed.LocationCategoryReviewedUpdate, db: Session = Depends(database.get_db)):
    """
    Actualiza una revisión de ubicación-categoría existente.

    - **location_id**: ID de la ubicación
    - **category_id**: ID de la categoría
    - **last_reviewed**: fecha de la última revisión
    """
    db_review = crud.get_location_category_reviewed(db, location_id=review.location_id, category_id=review.category_id)
    if not db_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return crud.update_location_category_reviewed(db=db, review=review)
