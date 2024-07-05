from pydantic import BaseModel, Field
from app.schemas import location

class CategoryBase(BaseModel):
    name: str = Field(..., description="Nombre de la categoría")
    description: str = Field(..., description="Descripción de la categoría")

    class Config:
        schema_extra = {
            "example": {
                "name": "Parques",
                "description": "Lugares de recreo al aire libre."
            }
        }

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    locations: list[location.Location] = []

    class Config:
        orm_mode = True