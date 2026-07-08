from fastapi import APIRouter,status
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
    
    )

router = APIRouter(
    prefix = "/users",
    tags=["Users"]
)


@router.post("/", status_code= status.HTTP_201_CREATED)
async def add_user(user: UserCreate):
    return create_user(user)

@router.get("/")
async def get_users():
    return get_all_users()

@router.get("/{user_id}")
async def get_user(user_id: str):
    return get_user_by_id(user_id)

@router.patch("/{user_id}")
async def edit_user( user_id:str, user:UserUpdate):
    return update_user(user_id, user)

@router.delete("/{user_id}")
async def remove_user(user_id: str):
    return delete_user(user_id)