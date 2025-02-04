from fastapi import APIRouter
from .endpoints import router as endpoints_router

router = APIRouter()

# Include endpoints
router.include_router(endpoints_router, prefix="/v1")