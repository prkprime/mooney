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
    description: str | None
    amount: float


class TransactionDatabase(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class TransactionRead(TransactionBase):
    id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(SQLModel):
    date: date | None
    category: TransactionType | None
    source: str | None
    description: str | None
    amount: str | None
