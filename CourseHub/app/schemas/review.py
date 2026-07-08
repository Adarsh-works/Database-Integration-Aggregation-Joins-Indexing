from bson import ObjectId
from pydantic import BaseModel, Field, field_validator

class ReviewCreate(BaseModel):
    userId: str
    courseId: str
    rating: int = Field(..., ge=1, le=5)
    comment: str = Field(..., min_length=5, max_length=500)

    @field_validator("userId", "courseId")
    @classmethod

    def validate_object_id(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return value
    
