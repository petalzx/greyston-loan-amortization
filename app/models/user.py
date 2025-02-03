from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    # Optional: Implement a feature that checks if user account is active (might be on hold)
    
    loans: Mapped[list["Loan"]] = relationship("Loan", back_populates="owner")
    shared_loans: Mapped[list["SharedLoan"]] = relationship("SharedLoan", back_populates="shared_with") 
