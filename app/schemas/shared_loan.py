from datetime import datetime
from pydantic import BaseModel


class SharedLoanCreate(BaseModel):
    loan_id: int
    shared_with_user_id: int


class SharedLoanResponse(BaseModel):
    id: int
    loan_id: int
    shared_with_user_id: int
    # is_created: datetime
    # is_updated: datetime

    class Config:
        from_attributes = True
