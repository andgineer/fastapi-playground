# fastapi-playground
For quick expreriments with FastAPI and Pydantic

## Local FastAPI
    . ./activate.sh
    make run

http://localhost:8000

also it started as service fastapi of docker-compose

## SQLModel
Service sqlmodel of docker-compose

    docker-compose up -d --build

http://localhost:8004/ping should return {"ping":"pong!"}

The application needs DB so easier to use docker-compose
Alternative you can run just DB with docker-compose and provide to the application correct
`DATABASE_URL` but that looks like overkill.
