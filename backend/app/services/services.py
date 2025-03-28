from core.config import db
from passlib.context import CryptContext
from db.models.user import User
from schemas.schemas import UserCreate, UserLogin, UserResponse
from fastapi import HTTPException, Depends, status, Response, Request
from typing import Optional
import uuid
import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")

    hashed_password = pwd_context.hash(user.password)

    recommendation_data = {
        "name": user.email,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }

    storage_data = {
        "name": user.email,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }

    new_recommendation = db.recommendations.insert_one(recommendation_data)
    recommendation_id = str(new_recommendation.inserted_id)

    new_storage = db.storage.insert_one(storage_data)
    storage_id = str(new_storage.inserted_id)

    user_data = {
        "email": user.email,
        "hashed_password": hashed_password,
        "recommendation_id": recommendation_id,
        "storage_id": storage_id
    }

    db.users.insert_one(user_data)

    return {
        "email": user.email,
        "recommendation_id": recommendation_id,
        "storage_id": storage_id,
        "message": "Пользователь успешно зарегистрирован"
    }    
def authenticate_user(user: UserLogin, response: Response):
    user_data = db.users.find_one({"email": user.email})
    if not user_data:
        raise HTTPException(status_code=401, detail="Пользователь не найден")
    if not pwd_context.verify(user.password, user_data["hashed_password"]):
        raise HTTPException(status_code=401, detail="Неверный пароль")
    session_data = {"user_email": user.email}
    response.set_cookie(
        key="session",
        value=user.email,
        httponly=True,
        max_age=1800,  # 30 минут
        samesite="lax"
    )
    return {"message": "Успешный вход в систему"}

def get_current_user(request: Request) -> Optional[str]:
    user_email = request.cookies.get("session")
    if not user_email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Не авторизован"
        )
    return user_email

def logout(response: Response):
    response.delete_cookie(key="session")
    return {"message": "Успешный выход из системы"}