from pydantic import BaseModel, Field
from datetime import datetime

class LocationCategoryReviewedBase(BaseModel):
    location_id: int = Field(..., description="ID de la ubicación")
    category_id: int = Field(..., description="ID de la categoría")
    last_reviewed: datetime = Field(..., description="Fecha de la última revisión")

    class Config:
        schema_extra = {
            "example": {
                "location_id": 1,
                "category_id": 1,
                "last_reviewed": "2024-07-01T00:00:00Z"
            }
        }

class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    last_reviewed: datetime = None

class LocationCategoryReviewedUpdate(LocationCategoryReviewedBase):
    last_reviewed: datetime = None 

class LocationCategoryReviewed(LocationCategoryReviewedBase):
    id: int

    class Config:
        orm_mode = True