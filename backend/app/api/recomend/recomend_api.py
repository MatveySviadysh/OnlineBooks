from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from core.config import get_database
from schemas.recomend import (
    RecommendationBase,
    RecommendationCreate,
    RecommendationUpdate,
    RecommendationResponse
)
from datetime import datetime
from bson import ObjectId

router = APIRouter(
    prefix="/recommend", 
    tags=["recommendation"],
    responses={404: {"description": "recommendation не найдена"}}
)

@router.post("/", response_model=RecommendationResponse)
async def create_recommendation(recommendation: RecommendationCreate, db=Depends(get_database)):
    existing_recommendation = await db.recommendations.find_one({"name": recommendation.name})
    if existing_recommendation:
        raise HTTPException(status_code=400, detail="Recommendation already exists")
    
    recommendation_dict = recommendation.dict()
    recommendation_dict["created_at"] = datetime.utcnow()
    recommendation_dict["updated_at"] = recommendation_dict["created_at"]
    
    new_recommendation = await db.recommendations.insert_one(recommendation_dict)
    created_recommendation = await db.recommendations.find_one({"_id": new_recommendation.inserted_id})
    created_recommendation["_id"] = str(created_recommendation["_id"])
    return RecommendationResponse(**created_recommendation)

@router.get("/", response_model=List[RecommendationResponse])
async def read_recommendations(email: Optional[str] = Query(None), db=Depends(get_database)):
    query = {"name": email} if email else {}
    recommendations_cursor = db.recommendations.find(query)
    recommendations = []
    async for recommendation in recommendations_cursor:
        recommendation["_id"] = str(recommendation["_id"])
        recommendations.append(RecommendationResponse(**recommendation))
    return recommendations

@router.delete("/", response_model=dict)
async def delete_all_recommendations(db=Depends(get_database)):
    result = await db.recommendations.delete_many({})
    return {"deleted_count": result.deleted_count, "message": "All recommendations have been deleted."}

@router.post("/{storage_id}/add-book/{book_id}", response_model=dict)
async def add_book_to_storage(storage_id: str, book_id: str, db=Depends(get_database)):
    try:
        storage = await db.recommendations.find_one({"_id": ObjectId(storage_id)})
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found")
        
        book = await db.books.find_one({"_id": ObjectId(book_id)})
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        if "books" not in storage:
            storage["books"] = []
            
        if book_id not in storage["books"]:
            result = await db.recommendations.update_one(
                {"_id": ObjectId(storage_id)},
                {"$push": {"books": book_id}}
            )
            if result.modified_count == 1:
                return {"message": "Book successfully added to storage"}
            else:
                raise HTTPException(status_code=400, detail="Failed to add book to storage")
        else:
            return {"message": "Book already exists in storage"}
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))