from bson import ObjectId

from pydantic import BaseModel, field_validator

class EnrollmentCreate(BaseModel):
    userId: str
    courseId: str


    @field_validator("userId", "courseId")
    @classmethod
    def validate_object_id(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Inavlid Object Id")
        return value
        