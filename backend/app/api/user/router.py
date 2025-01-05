from fastapi import APIRouter, Depends, Response, Request
from schemas.schemas import UserCreate, UserLogin, UserResponse
from services.services import create_user, authenticate_user, get_current_user, logout
from db.models.user import User

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