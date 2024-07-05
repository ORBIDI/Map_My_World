from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

    locations = relationship("Location", back_populates="category")

