from typing import Optional

from sqlmodel import SQLModel, Field
from datetime import date


class IncomeBase(SQLModel):
    date: date
    category: str
    source: str
    description: Optional[str]
    amount: float


class Income(IncomeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class IncomeRead(IncomeBase):
    id: int


class IncomeCreate(IncomeBase):
    pass


class IncomeUpdate(SQLModel):
    date: Optional[date]
    category: Optional[str]
    source: Optional[str]
    description: Optional[str]
    amount: Optional[float]
