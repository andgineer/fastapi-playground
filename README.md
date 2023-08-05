# fastapi-playground
For quick experiments with FastAPI, SQLModel and Pydantic

## Local FastAPI
    . ./activate.sh
    make run

The Swagger UI will be on http://localhost:8000

Also it started as service fastapi of docker-compose - see below.

## docker-compose
    docker-compose up -d --build

SQLModel application runs as service `sqlmodel` on port 8004, FastAPI application runs as service `fastapi` on port 8000.

## SQLModel
http://localhost:8004/ping should return {"ping":"pong!"}

The application needs DB so easier to use docker-compose
Alternative you can run just DB with docker-compose and provide to the application correct
`DATABASE_URL` but that looks like overkill.
