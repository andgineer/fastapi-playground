# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
- **Activate environment**: `. ./activate.sh` (must be sourced, not executed)
  - Creates `fastapi-playground` conda environment if it doesn't exist
  - Installs mamba if not available
  - Updates dependencies from `environment.yml`
  - Installs the package in editable mode with `pip install -e .`
- **Install dependencies**: `mamba env update -f environment.yml`
- **Upgrade dependencies**: `make reqs`

### Running Applications
- **FastAPI app**: `make run` (runs on port 8000 with Swagger UI at /)
- **SQLModel app**: `make sqlmodel` (requires DATABASE_URL environment variable)
- **Docker setup**: `docker-compose up -d --build` followed by `docker-compose exec sqlmodel alembic upgrade head`

### Code Quality
- **Linting**: `./scripts/lint.sh` (uses pre-commit hooks with ruff, mypy)
- **Pre-commit**: `pre-commit run --all-files`

### Testing
- **Run all tests**: `pytest`
- **Run with coverage**: `pytest --cov=fastapi_playground`
- **Run specific test file**: `pytest tests/test_main.py`
- **Run tests in verbose mode**: `pytest -v`

### Database Management
- **Connect to PostgreSQL**: `scripts/psql.sh`
- **View migration history**: `docker-compose exec sqlmodel alembic history -v`
- **Generate migration**: `docker-compose exec sqlmodel alembic revision --autogenerate -m "description"`

## Architecture

This is a FastAPI playground project with two separate applications:

### 1. Basic FastAPI App (`fastapi_playground.main`)
- Simple Pydantic model-based API
- Uses `humps` library for camelCase conversion in API responses
- Single User model with first_name, last_name, age
- No database persistence

### 2. SQLModel App (`fastapi_playground.sqlmodel`)
- Full database integration using SQLModel + SQLAlchemy async
- PostgreSQL backend with Alembic migrations
- Async session management via dependency injection
- User model with database table mapping
- Includes UserBase, User (table), and UserCreate models

### Key Components
- **Models**: Two separate model systems - Pydantic (`models.py`) and SQLModel (`sqlmodel/models.py`)
- **Database**: Async PostgreSQL with SQLAlchemy + SQLModel ORM
- **Migrations**: Alembic-based database migrations in `migrations/` directory
- **Tests**: Pytest-based test suite in `tests/` directory with fixtures for both apps
- **Environment**: Conda/mamba-based Python environment management

### Docker Services
- **FastAPI Service**: Port 8000 (basic app)
- **SQLModel Service**: Port 8004 (database-backed app)
- **PostgreSQL**: Port 5432

The project follows a dual-app pattern where you can experiment with both simple Pydantic models and full database-backed SQLModel implementations.
