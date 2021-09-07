from fastapi import APIRouter

from .endpoints import income, expense

api_router = APIRouter()

api_router.include_router(income.router, tags=["Income"])
api_router.include_router(expense.router, tags=["Expense"])
