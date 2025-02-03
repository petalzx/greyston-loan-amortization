
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) # Foreign Key to User
    amount: Mapped[float] = mapped_column()
    annual_interest_rate: Mapped[float] = mapped_column()
    term_months: Mapped[int] = mapped_column()

    owner: Mapped["User"] = relationship("User", back_populates="loans")
    shared_with: Mapped[list["SharedLoan"]] = relationship("SharedLoan", back_populates="loan")
