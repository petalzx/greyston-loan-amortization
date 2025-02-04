from typing import List, Dict
from app.schemas.loan import LoanStatus

def generate_amortization_schedule(amount: float, annual_interest_rate: float, term_months: int) -> List[Dict]:
    monthly_interest_rate = annual_interest_rate / 12 / 100

    # Fromula: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    monthly_payment = (
        amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** term_months)
        / ((1 + monthly_interest_rate) ** term_months - 1)
    )

    amortization_schedule = []
    remaining_balance = amount

    for month in range(1, term_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        amortization_schedule.append(
            {
                "month": month,
                "remaining_balance": round(remaining_balance, 2),
                "monthly_payment": round(monthly_payment, 2),
            }
        )

    return amortization_schedule


# def calculate_loan_summary(schedule: List[Dict], amount: float, month: int) -> Dict:
#     if month < 1 or month > len(schedule):
#         raise ValueError("Invalid month")

#     partial_schedule = schedule[:month]

#     # Total principal paid
#     total_principal_paid = amount - partial_schedule[-1]["remaining_balance"]

#     # Total interest paid (curently doesn't work)
#     total_interest_paid = sum(
#         item["monthly_payment"] - (partial_schedule[i - 1]
#                                    ["remaining_balance"] - item["remaining_balance"])
#         for i, item in enumerate(partial_schedule[1:], start=1)
#     )

#     current_principal_balance = partial_schedule[-1]["remaining_balance"]

#     status = LoanStatus.FINISHED if current_principal_balance <= 0 else LoanStatus.IN_PROGRESS

#     return {
#         "month": month,
#         "current_principal_balance": round(current_principal_balance, 2),
#         "total_principal_paid": round(total_principal_paid, 2),
#         "total_interest_paid": round(total_interest_paid, 2),
#         "status": status.value,  # .value gets the string representation of enum
#     }

def calculate_loan_summary(
    amount: float,
    annual_interest_rate: float,
    term_months: int,
    month: int
) -> Dict:
    if month < 1 or month > term_months:
        raise ValueError("Invalid month")

    monthly_interest_rate = annual_interest_rate / 12 / 100

    monthly_payment = (
        amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** term_months)
        / ((1 + monthly_interest_rate) ** term_months - 1)
    )

    remaining_balance = amount
    total_principal_paid = 0
    total_interest_paid = 0

    for _ in range(month):
        interest_payment = remaining_balance * monthly_interest_rate

        principal_payment = monthly_payment - interest_payment

        total_principal_paid += principal_payment
        total_interest_paid += interest_payment

        remaining_balance -= principal_payment

    # Loan status
    status = LoanStatus.FINISHED if remaining_balance <= 0 else LoanStatus.IN_PROGRESS

    return {
        "month": month,
        "current_principal_balance": round(remaining_balance, 2),
        "total_principal_paid": round(total_principal_paid, 2),
        "total_interest_paid": round(total_interest_paid, 2),
        "status": status.value,  # .value gets the string representation of enum
    }
