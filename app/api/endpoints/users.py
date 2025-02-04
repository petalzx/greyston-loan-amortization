from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import create_user, get_by_email
from app.schemas.user import UserCreate, UserResponse
from app.session import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{email}", response_model=UserResponse)
def get_by_email_endpoint(email: str, db: Session = Depends(get_db)):
    user = get_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user