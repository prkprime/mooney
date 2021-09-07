from typing import Optional

from sqlmodel import Field
from .income import IncomeBase, IncomeRead, IncomeUpdate, IncomeCreate


class ExpenseBase(IncomeBase):
    pass


class Expense(ExpenseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ExpenseRead(IncomeRead):
    pass


class ExpenseCreate(IncomeCreate):
    pass


class ExpenseUpdate(IncomeUpdate):
    pass
