from fastapi import APIRouter

from .endpoints import salary

api_router = APIRouter()

api_router.include_router(salary.router, tags=["salary"])
