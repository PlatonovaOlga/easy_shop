from fastapi import APIRouter
from .products import router as product_router
from .users import router as user_router

router = APIRouter()

router.include_router(
    product_router,
    prefix="/products")

router.include_router(
    user_router,
    prefix="/users"
)