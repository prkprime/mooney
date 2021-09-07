from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.models import Income, IncomeRead, IncomeCreate, IncomeUpdate
from app.database import engine

router = APIRouter()


@router.get("/income/", response_model=List[IncomeRead])
def get_income():
    with Session(engine) as s:
        return s.exec(select(Income)).all()


@router.post("/income/", response_model=IncomeRead)
def post_income(income: IncomeCreate):
    with Session(engine) as s:
        income_db = Income.from_orm(income)
        s.add(income_db)
        s.commit()
        s.refresh(income_db)
        return income_db


@router.get("/income/{income_id}", response_model=IncomeRead)
def get_single_income(income_id: int):
    with Session(engine) as s:
        income_db = s.get(Income, income_id)
        if not income_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="income transaction with given id does not exist",
            )
        return income_db


@router.patch("/income/{income_id}", response_model=IncomeRead)
def patch_income(income_id: int, income: IncomeUpdate):
    with Session(engine) as s:
        income_db = s.get(Income, income_id)
        if not income_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="income transaction with given id does not exist",
            )
        income_data = income.dict(exclude_unset=True)
        print(income_data)
        [setattr(income_db, k, v) for k, v in income_data.items()]
        s.add(income_db)
        s.commit()
        s.refresh(income_db)
        return income_db


@router.delete("/income/{income_id}", response_model=IncomeRead)
def delete_income(income_id: int):
    with Session(engine) as s:
        income_db = s.get(Income, income_id)
        if not income_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="income transaction with given id does not exist",
            )
        s.delete(income_db)
        s.commit()
        return income_db
