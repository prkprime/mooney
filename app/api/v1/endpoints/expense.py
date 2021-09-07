from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.models import Expense, ExpenseRead, ExpenseCreate, ExpenseUpdate
from app.database import engine

router = APIRouter()


@router.get("/expense/", response_model=List[ExpenseRead])
def get_expense():
    with Session(engine) as s:
        return s.exec(select(Expense)).all()


@router.post("/expense/", response_model=ExpenseRead)
def post_expense(expense: ExpenseCreate):
    with Session(engine) as s:
        expense_db = Expense.from_orm(expense)
        s.add(expense_db)
        s.commit()
        s.refresh(expense_db)
        return expense_db


@router.get("/expense/{expense_id}", response_model=ExpenseRead)
def get_single_expense(expense_id: int):
    with Session(engine) as s:
        expense_db = s.get(Expense, expense_id)
        if not expense_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="expense transaction with given id does not exist",
            )
        return expense_db


@router.patch("/expense/{expense_id}", response_model=ExpenseRead)
def patch_expense(expense_id: int, expense: ExpenseUpdate):
    with Session(engine) as s:
        expense_db = s.get(Expense, expense_id)
        if not expense_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="expense transaction with given id does not exist",
            )
        expense_data = expense.dict(exclude_unset=True)
        print(expense_data)
        [setattr(expense_db, k, v) for k, v in expense_data.items()]
        s.add(expense_db)
        s.commit()
        s.refresh(expense_db)
        return expense_db


@router.delete("/expense/{expense_id}", response_model=ExpenseRead)
def delete_expense(expense_id: int):
    with Session(engine) as s:
        expense_db = s.get(Expense, expense_id)
        if not expense_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="expense transaction with given id does not exist",
            )
        s.delete(expense_db)
        s.commit()
        return expense_db
