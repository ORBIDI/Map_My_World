from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database.database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="locations")

