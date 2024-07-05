from sqlalchemy.orm import Session

from ..models import reviewed as reviewedModel
from ..models import location as locationModel
from ..models import category as categoryModel

from datetime import datetime, timedelta
import logging

# Crear un logger
logger = logging.getLogger(__name__)

def get_recommendations(db: Session):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    logger.info("thirty_days_ago: %s", thirty_days_ago)
    subquery = db.query(reviewedModel.LocationCategoryReviewed.location_id, reviewedModel.LocationCategoryReviewed.category_id).filter(
       reviewedModel.LocationCategoryReviewed.last_reviewed >= thirty_days_ago
    ).subquery()

    logger.info("subquery: %s", subquery) 

    recommendations = db.query(locationModel.Location).join(
        categoryModel.Category, 
        locationModel.Location.category_id == categoryModel.Category.id         
    ).outerjoin(
        subquery, 
        (locationModel.Location.id == subquery.c.location_id) & 
        (categoryModel.Category.id == subquery.c.category_id)
    ).filter(
        subquery.c.location_id == None
    ).order_by(
        locationModel.Location.id.desc()
    ).limit(10).all()    

    return recommendations


