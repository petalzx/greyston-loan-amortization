from datetime import datetime, date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, NonNegativeFloat, PositiveInt, field_validator


class LoanCreate(BaseModel):
    amount: NonNegativeFloat
    annual_interest_rate: NonNegativeFloat
    term_months: PositiveInt
    # due_monthly_starting: date

    @field_validator('annual_interest_rate')
    def validate_interest_rate(cls, value):
        if value > 100:
            raise ValueError("Annual interest rate cannot exceed 100%")
        return value


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
