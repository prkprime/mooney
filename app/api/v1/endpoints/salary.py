from fastapi import APIRouter
from sqlmodel import Session, select
from typing import List

from app.models import Salary
from app.database import engine

router = APIRouter()


@router.get("/salary/", response_model=List[Salary])
def get_salary():
    with Session(engine) as s:
        return s.exec(select(Salary)).all()


@router.post("/salary/", status_code=200)
def post_salary(salary: Salary):
    with Session(engine) as s:
        s.add(salary)
        s.commit()
        s.refresh(salary)
        return salary
