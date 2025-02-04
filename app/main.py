from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.api import router as api_router
from app.session import SessionLocal

from app.models.database import Base
from app.session import engine

app = FastAPI(
    title="Loan Amortization API",
    description="An API for managing users, loans, and shared loans, with functionality to see amortization schedules.",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(api_router, prefix="/api")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Amortization API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )
