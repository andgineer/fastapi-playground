from fastapi import FastAPI, Depends

from fastapi_playground.sqlmodel.db import init_db, get_session
from sqlalchemy import select
from fastapi_playground.sqlmodel.models import User, UserCreate  # this import creates the table
from sqlmodel.ext.asyncio.session import AsyncSession

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/users", response_model=list[User])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [User(first_name=user.first_name, last_name=user.last_name, middle_name=user.middle_name, age=user.age) for user in users]


@app.post("/users")
async def add_song(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(first_name=user.first_name, last_name=user.last_name, age=user.age, middle_name=user.middle_name)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user