from typing import Optional

from sqlmodel import SQLModel, Field
from datetime import date


class Salary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    month: date
    Company: str
    earn_basic: float
    earn_special: float
    deduct_pf: float
    deduct_profession_tax: float
    deduct_voluntary_pf: float
    deduct_cf: float
    net_pay: float
