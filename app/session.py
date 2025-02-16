from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models.database import Base

# from app.core.config import settings

# Use in-memory SQLite instance atm
# DATABASE_URL = "sqlite:///:memory:?cache=shared"
DATABASE_URL = "sqlite:///./loan_amortization.db"

engine = create_engine(DATABASE_URL, echo=True)
# Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session = scoped_session(SessionLocal)


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
