from sqlalchemy.orm import Session
from app.models.shared_loan import SharedLoan
from app.schemas.shared_loan import SharedLoanCreate

def share_loan(db: Session, shared_loan: SharedLoanCreate):
    db_shared_loan = SharedLoan(**shared_loan.model_dump())
    db.add(db_shared_loan)
    db.commit()
    db.refresh(db_shared_loan)
    return db_shared_loan