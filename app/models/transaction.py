from typing import Optional

import enum

from sqlmodel import SQLModel, Field
from datetime import date


class TransactionType(str, enum.Enum):
    expense: str = "expense"
    income: str = "income"


class TransactionBase(SQLModel):
    date: date
    category: TransactionType
    source: str
    description: Optional[str]
    amount: float


class TransactionDatabase(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TransactionRead(TransactionBase):
    id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(SQLModel):
    date: Optional[date]
    category: Optional[TransactionType]
    source: Optional[str]
    description: Optional[str]
    amount: Optional[float]
