from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi_playground.sqlmodel.db import get_session, init_db
from fastapi_playground.sqlmodel.models import User, UserCreate  # this import creates the table

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


get_session_dependency = Depends(get_session)


@app.get("/songs", response_model=list[User])
async def get_songs(session: AsyncSession = get_session_dependency):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [
        User(
            first_name=user.first_name,
            last_name=user.last_name,
            middle_name=user.middle_name,
            age=user.age,
        )
        for user in users
    ]


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
