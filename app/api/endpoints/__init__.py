from fastapi import APIRouter
from .users import router as users_router
from .loans import router as loans_router
from .shared_loans import router as shared_loans_router

router = APIRouter()

router.include_router(users_router)
router.include_router(loans_router)
router.include_router(shared_loans_router)