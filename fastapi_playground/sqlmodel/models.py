from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    first_name: str
    last_name: str
    age: int

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)

    first_name: str
    last_name: str
    middle_name: str
    age: int


class UserCreate(UserBase):
    pass
