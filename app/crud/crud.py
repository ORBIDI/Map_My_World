from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_, func

from ..schemas import location
from ..schemas import category
from ..schemas import reviewed

from ..models import reviewed as reviewedModel
from ..models import location as locationModel
from ..models import category as categoryModel

from datetime import datetime, timedelta

def get_category(db: Session, category_id: int):
    return db.query(categoryModel.Category).filter(categoryModel.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(categoryModel.Category).offset(skip).limit(limit).all()

def get_category_by_name(db: Session, name: str):
    return db.query(categoryModel.Category).filter(categoryModel.Category.name == name).first()

def create_category(db: Session, category: category.CategoryCreate):
    # Verificar si la categoría ya existe
    existing_category = get_category_by_name(db, name=category.name)
    if existing_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists"
        )
    db_category = categoryModel.Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_location(db: Session, location_id: int):
    return db.query(locationModel.Location).filter(locationModel.Location.id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(locationModel.Location).offset(skip).limit(limit).all()

def get_location_by_name(db: Session, name: str):
    return db.query(locationModel.Location).filter(locationModel.Location.name == name).first()

def create_location(db: Session, location: location.LocationCreate):
    # Verificar si la ubicación ya existe
    existing_location = get_location_by_name(db, name=location.name)
    if existing_location:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Location already exists"
        )
    db_location = locationModel.Location(name=location.name, description=location.description, latitude=location.latitude, longitude=location.longitude, category_id=location.category_id)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def create_review(db: Session, review: reviewed.LocationCategoryReviewedCreate):
    db_review = reviewedModel.LocationCategoryReviewed(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session, skip: int = 0, limit: int = 10):
    return db.query(reviewedModel.LocationCategoryReviewed).offset(skip).limit(limit).all()

def get_recommendations(db: Session, category_id: int):
    return db.query(locationModel.Location).filter(locationModel.Location.category_id == category_id).order_by(locationModel.Location.id.desc()).limit(10).all()


def get_location_category_reviewed(db: Session, location_id: int, category_id: int):
    return db.query(reviewedModel.LocationCategoryReviewed).filter(
        reviewedModel.LocationCategoryReviewed.location_id == location_id,
        reviewedModel.LocationCategoryReviewed.category_id == category_id
    ).first()

def create_location_category_reviewed(db: Session, review: reviewed.LocationCategoryReviewedCreate):
    db_review = reviewedModel.LocationCategoryReviewed(location_id=review.location_id, category_id=review.category_id, last_reviewed=review.last_reviewed)
    db_review.last_reviewed = datetime.utcnow()
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_location_category_reviewed(db: Session, review: reviewed.LocationCategoryReviewedUpdate):
    db_review = db.query(reviewedModel.LocationCategoryReviewed).filter(
        reviewedModel.LocationCategoryReviewed.location_id == review.location_id,
        reviewedModel.LocationCategoryReviewed.category_id == review.category_id
    ).first()
    if db_review:
        db_review.last_reviewed = datetime.utcnow()
        db.commit()
        db.refresh(db_review)
    return db_review

def get_exploration_recommendations(db: Session, limit: int = 10):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    # Subquery to find location-category pairs that have been reviewed in the last 30 days
    recent_reviews_subquery = db.query(reviewedModel.LocationCategoryReviewed.location_id, reviewedModel.LocationCategoryReviewed.category_id)\
        .filter(reviewedModel.LocationCategoryReviewed.reviewed_at >= thirty_days_ago).subquery()
    
    # Main query to find location-category pairs that haven't been reviewed in the last 30 days
    recommendations = db.query(locationModel.Location, categoryModel.Category)\
        .outerjoin(recent_reviews_subquery,
                   and_(locationModel.Location.id == recent_reviews_subquery.c.location_id,
                        models.Location.category_id == recent_reviews_subquery.c.category_id))\
        .filter(recent_reviews_subquery.c.location_id == None)\
        .order_by(func.random())\
        .limit(limit)\
        .all()
    
    # If we don't have enough results, add more that were reviewed the longest time ago
    if len(recommendations) < limit:
        additional_recommendations = db.query(locationModel.Location, categoryModel.Category)\
            .outerjoin(reviewedModel.LocationCategoryReviewed,
                       and_(locationModel.Location.id == reviewedModel.LocationCategoryReviewed.location_id,
                            locationModel.Location.category_id == reviewedModel.LocationCategoryReviewed.category_id))\
            .order_by(reviewedModel.LocationCategoryReviewed.reviewed_at.asc())\
            .limit(limit - len(recommendations))\
            .all()
        
        recommendations.extend(additional_recommendations)
    
    return recommendations
