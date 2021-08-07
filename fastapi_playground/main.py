import uvicorn
from fastapi import FastAPI

from fastapi_playground.models import User

__version__ = "1.1"

app = FastAPI(
    docs_url="/",
    version=__version__,
)


@app.post("/user/", response_model=User)
async def create_user(user: User):
    return User(firstName=user.first_name, last_name="Smith", age=user.age)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
