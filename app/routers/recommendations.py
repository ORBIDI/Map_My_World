from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import location

from ..services import recommendations
from ..database import database

router = APIRouter(
    prefix="/recommendations",
    tags=["Recomendaciones"]
)

@router.get("/", response_model=list[location.Location], summary="Obtener recomendaciones de exploración")
def get_recommendations(db: Session = Depends(database.get_db)):
    """
    Obtiene recomendaciones de exploración de ubicación-categoría que no han sido revisadas en los últimos 30 días.
    """
    return recommendations.get_recommendations(db)

