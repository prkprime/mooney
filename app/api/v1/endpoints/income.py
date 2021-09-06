from fastapi import APIRouter
from sqlmodel import Session, select
from typing import List

from app.models import Income, IncomeRead, IncomeCreate, IncomeUpdate
from app.database import engine

router = APIRouter()


@router.get("/income/", response_model=List[IncomeRead])
def get_salary():
    with Session(engine) as s:
        return s.exec(select(Income)).all()


@router.post("/income/", response_model=IncomeRead)
def post_salary(income: IncomeCreate):
    with Session(engine) as s:
        income_db = Income.from_orm(income)
        s.add(income_db)
        s.commit()
        s.refresh(income_db)
        return income_db
