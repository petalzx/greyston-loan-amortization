from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class SharedLoan(Base):
    __tablename__ = "shared_loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    loan_id: Mapped[int] = mapped_column(ForeignKey="loans.id")
    shared_with_user_id: Mapped[int] = mapped_column(ForeignKey="users.id")

    # Relationships
    loan: Mapped["Loan"] = relationship("Loan", back_populates="shared_with")
    shared_with: Mapped["User"] = relationship(
        "User", back_populates="shared_loans")
