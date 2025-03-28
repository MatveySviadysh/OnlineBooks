from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from core.config import get_database
from schemas.storage import (
    StorageBase,
    StorageCreate,
    StorageUpdate,
    StorageResponse
)
from datetime import datetime
from bson import ObjectId
from urllib.parse import unquote
import logging



router = APIRouter(
    prefix="/storage",
    tags=["storage"],
    responses={404: {"description": "Storage не найден"}}
)

@router.post("/", response_model=StorageResponse)
async def create_storage(storage: StorageCreate, db=Depends(get_database)):
    existing_storage = await db.storage.find_one({"name": storage.name})
    if existing_storage:
        raise HTTPException(status_code=400, detail="Storage already exists")
    
    storage_dict = storage.dict()
    storage_dict["created_at"] = datetime.utcnow()
    storage_dict["updated_at"] = storage_dict["created_at"]
    
    new_storage = await db.storage.insert_one(storage_dict)
    created_storage = await db.storage.find_one({"_id": new_storage.inserted_id})
    created_storage["_id"] = str(created_storage["_id"])
    return StorageResponse(**created_storage)

@router.get("/", response_model=List[StorageResponse])
async def read_storages(name: Optional[str] = Query(None), db=Depends(get_database)):
    query = {"name": name} if name else {}
    storages_cursor = db.storage.find(query)
    storages = []
    
    async for storage in storages_cursor:
        storage["_id"] = str(storage["_id"])  # Convert ObjectId to string
        
        if 'user_id' not in storage:
            storage['user_id'] = 0  # Assuming 0 as default for now, change if necessary

        try:
            storage['user_id'] = int(storage['user_id'])  # Convert to integer if it's a string
        except ValueError:
            logging.error(f"Invalid user_id value: {storage['user_id']} for storage {_id}")
            storage['user_id'] = 0  # Default to 0 in case of error

        storages.append(StorageResponse(**storage))
    
    return storages

@router.post("/{storage_id}/add-item/{item_id}", response_model=StorageResponse)
async def add_item_to_storage(storage_id: str, item_id: str, db=Depends(get_database)):
    try:
        storage = await db.storage.find_one({"_id": ObjectId(storage_id)})
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found")
        
        item = await db.items.find_one({"_id": ObjectId(item_id)})
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        if "item_ids" not in storage:
            storage["item_ids"] = []
            
        if item_id not in storage["item_ids"]:
            await db.storage.update_one(
                {"_id": ObjectId(storage_id)},
                {
                    "$push": {"item_ids": item_id},
                    "$set": {"updated_at": datetime.utcnow()}
                }
            )
        
        updated_storage = await db.storage.find_one({"_id": ObjectId(storage_id)})
        updated_storage["_id"] = str(updated_storage["_id"])
        return StorageResponse(**updated_storage)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{storage_id}/add-book/{book_id}", response_model=StorageResponse)
async def add_book_to_storage(storage_id: str, book_id: str, db=Depends(get_database)):
    try:
        storage_oid = ObjectId(storage_id)
        book_oid = ObjectId(book_id)

        storage = await db.storage.find_one({"_id": storage_oid})
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found")

        book = await db.books.find_one({"_id": book_oid})
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        if "book_ids" not in storage:
            storage["book_ids"] = []

        if book_id not in storage["book_ids"]:
            await db.storage.update_one(
                {"_id": storage_oid},
                {
                    "$push": {"book_ids": book_id},
                    "$set": {"updated_at": datetime.utcnow()}
                }
            )

        updated_storage = await db.storage.find_one({"_id": storage_oid})
        updated_storage["_id"] = str(updated_storage["_id"])  # Преобразуем ObjectId в строку
        return StorageResponse(**updated_storage)  # Возвращаем обновленное хранилище

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка: {str(e)}")


@router.get("/books-by-email/{email}", response_model=List[str])
async def get_books_by_email(email: str, db=Depends(get_database)):
    try:
        storage = await db.storage.find_one({"name": email})
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found for this email")
        
        book_ids = storage.get("book_ids", [])
        return book_ids
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/storage-id-by-email/{email}", response_model=str)
async def get_storage_id_by_email(email: str, db=Depends(get_database)):
    try:
        storage = await db.storage.find_one({"name": email})
        
        if not storage:
            raise HTTPException(status_code=404, detail="Storage not found for this email")
        
        return str(storage["_id"])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
