from fastapi import APIRouter
from .endpoints.users import router as users_router
from .endpoints.loans import router as loans_router
from .endpoints.shared_loans import router as shared_loans_router

router = APIRouter()

router.include_router(users_router, prefix="/endpoints")
router.include_router(loans_router, prefix="/endpoints")
router.include_router(shared_loans_router, prefix="/endpoints")