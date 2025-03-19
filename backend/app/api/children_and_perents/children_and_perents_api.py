from fastapi import APIRouter, Depends, HTTPException
from typing import List
from core.config import get_database
from db.models.children_and_perents import ChildrenAndPerents

router = APIRouter(
    prefix="/children_and_perents",
    tags=["children_and_perents"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=ChildrenAndPerents)
async def create_children_and_perents(item: ChildrenAndPerents, db=Depends(get_database)):
    existing_record = await db.children_and_perents.find_one({})
    if existing_record:
        raise HTTPException(status_code=400, detail="Record already exists. Only one record is allowed.")
    
    new_item = await db.children_and_perents.insert_one(item.dict())
    created_item = await db.children_and_perents.find_one({"_id": new_item.inserted_id})
    return ChildrenAndPerents(**{**created_item, "_id": str(created_item["_id"])})

@router.get("/", response_model=ChildrenAndPerents)
async def read_children_and_perents(db=Depends(get_database)):
    item = await db.children_and_perents.find_one({})
    if item is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return ChildrenAndPerents(**{**item, "_id": str(item["_id"])})

@router.put("/", response_model=ChildrenAndPerents)
async def update_children_and_perents(item: ChildrenAndPerents, db=Depends(get_database)):
    existing_item = await db.children_and_perents.find_one({})
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Record not found")
    
    update_result = await db.children_and_perents.update_one(
        {"_id": existing_item["_id"]},
        {"$set": item.dict()}
    )
    
    if update_result.modified_count == 1:
        updated_item = await db.children_and_perents.find_one({"_id": existing_item["_id"]})
        return ChildrenAndPerents(**{**updated_item, "_id": str(updated_item["_id"])})
    raise HTTPException(status_code=400, detail="Update failed")

@router.delete("/", response_model=dict)
async def delete_children_and_perents(db=Depends(get_database)):
    result = await db.children_and_perents.delete_many({})
    return {"deleted_count": result.deleted_count, "message": "Record has been deleted"}