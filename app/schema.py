from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=60)

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2)
    age: Optional[int] = Field(None, ge=18)
