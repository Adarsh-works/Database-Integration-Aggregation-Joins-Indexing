from fastapi import HTTPException, status
from app.core.db import database
from app.utils.helpers import serialize_doc
from app.utils.helpers import serialize_docs
from app.schemas.user import UserCreate
from bson import ObjectId
from app.schemas.user import UserUpdate

users_collection = database["users"]

def create_user(user: UserCreate):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )
    if existing_user:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Email already registered"
        )
    
    result = users_collection.insert_one(
        user.model_dump()
    )
    created_user = users_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_doc(created_user)


def get_all_users():
    users = users_collection.find()
    return serialize_docs(users)


def get_user_by_id(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Invalid user ID"
        )
    user= users_collection.find_one(
            {"_id": ObjectId(user_id)}
        )
    if not user:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "User not found"
            )
    return serialize_doc(user)

def update_user(user_id: str, user: UserUpdate):

    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Invalid user ID"
            
        )
    update_data = user.model_dump(exclude_unset = True)

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )
    updated_user= users_collection.find_one(
        {"_id": ObjectId(user_id)}
    )
    return serialize_doc(updated_user)

def delete_user(user_id: str):

    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Invalid user ID"
        )
    result = users_collection.delete_one(
        {"_id": ObjectId(user_id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
    return {
        "message": "User deleted successfully"
    }