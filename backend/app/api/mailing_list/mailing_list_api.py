from fastapi import APIRouter, Depends, HTTPException
from typing import List
from core.config import get_database
from db.models.mailing_list import UserEmail

router = APIRouter(
    prefix="/mailing_list", 
    tags=["mailing_list"],
    responses={404: {"description": "список не найден"}}
)

@router.post("/emails/", response_model=UserEmail)
async def create_email(email: UserEmail, db=Depends(get_database)):
    existing_email = await db.emails.find_one({"email": email.email})
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_email = await db.emails.insert_one(email.dict(exclude={"id"}))
    email.id = str(new_email.inserted_id)
    return email

@router.get("/emails/", response_model=List[UserEmail])
async def read_emails(db=Depends(get_database)):
    emails_cursor = db.emails.find()
    emails = [UserEmail(**{**email, "_id": str(email["_id"])}) async for email in emails_cursor]
    return emails

@router.delete("/emails/", response_model=dict)
async def delete_all_emails(db=Depends(get_database)):
    result = await db.emails.delete_many({})
    return {"deleted_count": result.deleted_count, "message": "All emails have been deleted."}