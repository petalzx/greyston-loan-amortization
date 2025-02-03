
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column()
    annual_interest_rate: Mapped[float] = mapped_column()
    term_months: Mapped[int] = mapped_column()


