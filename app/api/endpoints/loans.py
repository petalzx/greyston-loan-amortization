from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.loan_service import (
    create_loan,
    get_loan_schedule,
    get_loan_summary,
)
from app.schemas.loan import LoanCreate, LoanScheduleItem, LoanMonthSummary
from app.session import get_db

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/", response_model=LoanCreate)
def create_loan_endpoint(loan: LoanCreate, db: Session = Depends(get_db), user_id: int = 1):
    return create_loan(db, loan, user_id)

@router.get("/{loan_id}/schedule", response_model=list[LoanScheduleItem])
def get_loan_schedule_endpoint(loan_id: int, db: Session = Depends(get_db)):
    schedule = get_loan_schedule(db, loan_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Loan not found")
    return schedule

@router.get("/{loan_id}/summary", response_model=LoanMonthSummary)
def get_loan_summary_endpoint(loan_id: int, month: int, db: Session = Depends(get_db)):
    summary = get_loan_summary(db, loan_id, month)
    if not summary:
        raise HTTPException(status_code=404, detail="Loan not found")
    return summary