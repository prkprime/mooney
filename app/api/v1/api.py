from fastapi import APIRouter

from .endpoints import income

api_router = APIRouter()

api_router.include_router(income.router, tags=["Income"])
