from datetime import datetime, date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, NonNegativeFloat, PositiveInt


class LoanCreate(BaseModel):
    amount: NonNegativeFloat
    annual_interest_rate: NonNegativeFloat
    term_months: PositiveInt
    # due_monthly_starting: date


class LoanResponse(BaseModel):
    id: str
    amount: NonNegativeFloat
    annual_interest_rate: NonNegativeFloat
    term_months: PositiveInt
    due_monthly_starting: date
    # is_created: datetime
    # is_updated: datetime
    
    # Not really sure how the owner_id should be implemented atp
    owner_id: int

    class Config:
        from_attributes = True


class LoanScheduleItem(BaseModel):
    month: PositiveInt
    remaining_balance: NonNegativeFloat
    monthly_payment: NonNegativeFloat

class LoanStatus(Enum):
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"

class LoanMonthSummary(BaseModel):
    month: PositiveInt
    current_principal_balance: NonNegativeFloat
    total_principal_paid: NonNegativeFloat
    total_interest_paid: NonNegativeFloat
    status: LoanStatus
