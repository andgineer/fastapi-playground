from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    first_name: str
    last_name: str = Field(default=None, nullable=True)
    middle_name: str
    age: int

class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass
