from pydantic import BaseModel, Field

class LocationBase(BaseModel):
    name: str = Field(..., description="Nombre de la ubicación")
    description: str = Field(..., description="Descripción de la ubicación")
    latitude: float = Field(..., description="Latitud de la ubicación")
    longitude: float = Field(..., description="Longitud de la ubicación")
    category_id: int = Field(..., description="ID de la categoría a la que pertenece la ubicación")

    class Config:
        schema_extra = {
            "example": {
                "name": "Central Park",
                "description": "Un gran parque en el centro de la ciudad.",
                "latitude": 40.785091,
                "longitude": -73.968285,
                "category_id": 1
            }
        }

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True