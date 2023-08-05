from fastapi import FastAPI

from fastapi_playground.sqlmodel.db import init_db
from fastapi_playground.sqlmodel.models import User  # this import creates the table

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
