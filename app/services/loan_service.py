from typing import Optional

from sqlalchemy.orm import Session
from app.schemas.loan import LoanCreate, LoanScheduleItem, LoanMonthSummary
from app.utils.amortization import generate_amortization_schedule, create_loan_month_summary

