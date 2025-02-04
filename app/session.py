from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

#from app.core.config import settings

# Use in-memory SQLite instance atm
DATABASE_URL = "sqlite://"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = scoped_session(SessionLocal)


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

