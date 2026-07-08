from pydantic import BaseModel, Field, field_validator
from bson import ObjectId

class Lesson(BaseModel):
    title: str = Field(..., min_length=3)
    duration: int = Field(..., gt=0)


class CourseCreate(BaseModel):
    title: str = Field(...,min_length=3)
    description: str = Field(..., min_length=20)
    price: float = Field(..., gt=0)
    instructorId: str
    lessons: list[Lesson]

    @field_validator("instructorId")
    @classmethod
    def validate_object_id(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid instructor ID")
        return value