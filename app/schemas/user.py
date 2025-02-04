from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

# Base schema for common fields
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str # Need to hash before saving to DB

class UserResponse(UserBase):
    id: int

    # Might not use this, extra documentation functionality
    # created_at: Optional[datetime]
    # updated_at: Optional[datetime]

    class Config:
        from_attributes = True


