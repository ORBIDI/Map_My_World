from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database.database import Base
from datetime import datetime

class LocationCategoryReviewed(Base):
    __tablename__ = "location_category_reviewed"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    last_reviewed = Column(DateTime, default=datetime.utcnow)

    location = relationship("Location")
    category = relationship("Category")