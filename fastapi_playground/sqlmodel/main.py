from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi_playground.sqlmodel.db import get_session, init_db
from fastapi_playground.sqlmodel.models import User, UserCreate  # this import creates the table

app = FastAPI()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_db()
    yield


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


get_session_dependency = Depends(get_session)


@app.get("/songs", response_model=list[User])
async def get_songs(session: AsyncSession = get_session_dependency):
    result = await session.exec(select(User))
    return result.all()


@app.post("/songs")
async def add_song(user: UserCreate, session: AsyncSession = get_session_dependency):
    user = User(  # type: ignore
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        middle_name=user.middle_name,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
