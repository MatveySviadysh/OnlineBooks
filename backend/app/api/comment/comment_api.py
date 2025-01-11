from fastapi import APIRouter, Depends, HTTPException
from typing import List
from core.config import get_database
from schemas.comment import CommentCreate, CommentUpdate, CommentResponse
from crud.crud_comment import get_comment_crud, CRUDComment

router = APIRouter(
    prefix="/comments", 
    tags=["comments"],
    responses={404: {"description": "Комментарий не найден"}}
)

async def get_crud_comment(db=Depends(get_database)):
    return get_comment_crud(db)

@router.post("/", response_model=CommentResponse)
async def create_comment(comment: CommentCreate, crud: CRUDComment = Depends(get_crud_comment)):
    return await crud.create_comment(comment)

@router.get("/{comment_id}", response_model=CommentResponse)
async def read_comment(comment_id: str, crud: CRUDComment = Depends(get_crud_comment)):
    return await crud.get_comment(comment_id)

@router.put("/{comment_id}", response_model=CommentResponse)
async def update_comment(comment_id: str, comment_update: CommentUpdate, crud: CRUDComment = Depends(get_crud_comment)):
    return await crud.update_comment(comment_id, comment_update)

@router.delete("/{comment_id}", response_model=dict)
async def delete_comment(comment_id: str, crud: CRUDComment = Depends(get_crud_comment)):
    return await crud.delete_comment(comment_id)

@router.get("/", response_model=List[CommentResponse])
async def list_comments(skip: int = 0, limit: int = 10, crud: CRUDComment = Depends(get_crud_comment)):
    return await crud.list_comments(skip=skip, limit=limit)
