# FastAPI Playground
A sandbox environment for experimenting with FastAPI, SQLModel, and Pydantic.

Perfect for testing ideas, prototyping features, and learning the stack.

## Quick Start
### Local Development
    . ./activate.sh

    # FastAPI: Swagger UI at http://localhost:8000
    make run

    # SQLMoldel: Swagger UI at http://localhost:8000/docs
    make sqlmodel

### Docker Setup
    docker-compose up -d --build
    docker-compose exec sqlmodel alembic upgrade head  # Initialize database tables

#### Docker Compose Services
- **SQLModel Service**: Runs on port 8004
- **FastAPI Service**: Runs on port 8000

Test the SQLModel Service health with:

    curl http://localhost:8004/ping

Expected response: {"ping":"pong!"}

## Database Setup

### PostgreSQL Client Installation
**macOS:**
    brew doctor
    brew update
    brew install libpq
    echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.zshrc

**Configure PostgreSQL password file:**
    cp .pgpass ~/.pgpass
    chmod 600 ~/.pgpass

### Database Management
**Connect to PostgreSQL:**
    scripts/psql.sh

**View User table structure:**
    \d+ User

## 🔄 Database Migrations (Alembic)

### Common Commands
**View migration history:**
    docker-compose exec sqlmodel alembic history -v

**Generate new migration:**
    docker-compose exec sqlmodel alembic revision --autogenerate -m "description"
