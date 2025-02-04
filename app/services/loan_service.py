from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.loan import Loan
from app.schemas.loan import LoanCreate, LoanScheduleItem, LoanMonthSummary
from app.utils.amortization import generate_amortization_schedule, calculate_loan_summary


def create_loan(db: Session, loan: LoanCreate, user_id: int) -> Loan:
    db_loan = Loan(**loan.model_dump(), user_id=user_id)
    db.add(db_loan)
    db.commit()
    db.refresh()
    return db_loan


def get_loan_schedule(db: Session, loan_id: int) -> Optional[List[LoanScheduleItem]]:
    loan = db.query(Loan).filter(Loan.id == loan_id).one_or_none()
    if not loan:
        return None

    schedule = generate_amortization_schedule(
        loan.amount, loan.annual_interest_rate, loan.term_months)

    return [LoanScheduleItem(**item) for item in schedule]


def get_loan_summary(db: Session, loan_id: int, month: int) -> Optional[LoanMonthSummary]:
    loan = db.query(Loan).filter(Loan.id == loan_id).one_or_none()
    if not loan:
        return None

    schedule = generate_amortization_schedule(
        loan.amount, loan.annual_interest_rate, loan.term_months
    )

    summary = calculate_loan_summary(schedule, loan.amount, month)
    return LoanMonthSummary(**summary)
