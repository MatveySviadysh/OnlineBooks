from fastapi import APIRouter, Depends, Response, Request
from schemas.schemas import UserCreate, UserLogin, UserResponse
from services.services import create_user, authenticate_user, get_current_user, logout
from db.models.user import User
from core.config import get_database
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    return create_user(user)

@router.post("/login")
async def login(user: UserLogin, response: Response):
    return authenticate_user(user, response)

@router.post("/logout")
async def logout_user(response: Response):
    return logout(response)

@router.get("/me")
async def get_user_me(request: Request):
    user_email = get_current_user(request)
    return {"email": user_email}

@router.get("/exists/{email}", response_model=bool)
async def exists_user(email: str, db: Session = Depends(get_database)):
    user = await db.users.find_one({"email": email})  # Используйте переданный email
    exists = user is not None
    return exists


@router.get("/exists/id/{user_id}", response_model=bool)
async def exists_user_by_id(user_id: int, db: Session = Depends(get_database)):
    user = db.query(User).filter(User.id == user_id)  # Убедитесь, что вы используете db из зависимости
    return user is not None