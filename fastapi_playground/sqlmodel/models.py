from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    first_name: str
    last_name: Optional[str] = Field(default=None, nullable=True)
    middle_name: str
    age: int


class User(UserBase, table=True):  # type: ignore
    id: Optional[int] = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass
