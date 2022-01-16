import enum
from typing import List

from pydantic import EmailStr
from pydantic import validator
from sqlmodel import SQLModel
from sqlmodel import Field

class UserBase(SQLModel):
    username: str = Field(index=True)
    email: EmailStr = Field(index=True)
    display_name: str

    @validator("username")
    def validate_username(cls, username: str) -> str:
        if len(username) < 4 or len(username) > 24:
            raise ValueError("Username must be 4-24 characters long.")
        if not username.isalnum():
            raise ValueError("Username can only contain letters and numbers. No special characters are allowed.")
        return username

class UserDatabase(UserBase, table=True):
    id : int | None = Field(default=None, primary_key=True)
    password: str

class UserRead(UserBase):
    id: int
def contains_illeagal_characters(password : str) -> bool:
    allowed_characters = ["!", "#", "-", "@", ".", ",", ":", ";", "$", "&", "%", "*"]
    for i in password:
        if not i.isalnum():
            if i not in allowed_characters:
                return True
    return False

def validate_password(password: str | None) -> str | None:
    if password:
        if len(password) < 8:
            raise ValueError("Password must contain atleast 8 characters!")
        digit_count = sum(x.isdigit() for x in password)
        lower_count = sum(x.islower() for x in password)
        upper_count = sum(x.isupper() for x in password)
        if digit_count < 1 or lower_count < 1 or upper_count < 1 or contains_illeagal_characters(password):
            raise ValueError("Password must contain one uppercase letter, one lowercase letter, one digit and one of the following special characters ('!'', '#', '-', '@', '.', ',', ':', ';', '$', '&', '%', '*')")
    return password

class UserCreate(UserBase):
    password: str = validator("password", allow_reuse=True)(validate_password)

class UserUpdate(UserBase):
    username: str | None
    email: EmailStr | None
    display_name: str | None
    password: str | None = validator("password", allow_reuse=True)(validate_password)