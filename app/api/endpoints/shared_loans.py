from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.shared_loan_service import share_loan
from app.schemas.shared_loan import SharedLoanCreate, SharedLoanResponse
from app.session import get_db

router = APIRouter(prefix="/shared-loans", tags=["shared_loans"])

@router.post("/", response_model=SharedLoanResponse)
def share_loan_endpoint(shared_loan: SharedLoanCreate, db: Session = Depends(get_db)):
    return share_loan(db, shared_loan)