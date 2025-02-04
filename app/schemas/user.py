from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator

# Base schema for common fields
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str # Need to hash before saving to DB

    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

class UserResponse(UserBase):
    id: int

    # Might not use this, extra documentation functionality
    # created_at: Optional[datetime]
    # updated_at: Optional[datetime]

    class Config:
        from_attributes = True


