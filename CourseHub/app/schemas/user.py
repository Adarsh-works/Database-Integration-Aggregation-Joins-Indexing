from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    role: str = Field(..., pattern="^(student|instructor)$")

class UserUpdate(BaseModel):
        name: Optional[str] = Field(None, min_length=2, max_length=50)
        email: Optional[EmailStr] = None
        role: Optional[str] = Field(None, pattern="^(student|instructor)$")