from fastapi import APIRouter

from .endpoints import transaction

api_router = APIRouter()

api_router.include_router(transaction.router, tags=["Transaction"])
