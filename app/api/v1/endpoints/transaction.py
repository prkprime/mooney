from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.models import (
    TransactionDatabase,
    TransactionRead,
    TransactionCreate,
    TransactionUpdate,
)
from app.database import engine

router = APIRouter()


@router.get("/transaction/", response_model=List[TransactionRead])
def get_transaction():
    with Session(engine) as s:
        return s.exec(select(TransactionDatabase)).all()


@router.post("/transaction/", response_model=TransactionRead)
def post_transaction(transaction: TransactionCreate):
    with Session(engine) as s:
        transaction_db = TransactionDatabase.from_orm(transaction)
        s.add(transaction_db)
        s.commit()
        s.refresh(transaction_db)
        return transaction_db


@router.get("/transaction/{transaction_id}", response_model=TransactionRead)
def get_single_transaction(transaction_id: int):
    with Session(engine) as s:
        transaction_db = s.get(TransactionDatabase, transaction_id)
        if not transaction_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="transaction with given id does not exist",
            )
        return transaction_db


@router.patch("/transaction/{transaction_id}", response_model=TransactionRead)
def patch_transaction(transaction_id: int, transaction: TransactionUpdate):
    with Session(engine) as s:
        transaction_db = s.get(TransactionDatabase, transaction_id)
        if not transaction_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="transaction with given id does not exist",
            )
        transaction_data = transaction.dict(exclude_unset=True)
        print(transaction_data)
        [setattr(transaction_db, k, v) for k, v in transaction_data.items()]
        s.add(transaction_db)
        s.commit()
        s.refresh(transaction_db)
        return transaction_db


@router.delete("/transaction/{transaction_id}", response_model=TransactionRead)
def delete_transaction(transaction_id: int):
    with Session(engine) as s:
        transaction_db = s.get(TransactionDatabase, transaction_id)
        if not transaction_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="transaction with given id does not exist",
            )
        s.delete(transaction_db)
        s.commit()
        return transaction_db
