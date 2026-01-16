1) pip install poetry
add to envirornmental variables path (C:\Users\bhavy\AppData\Roaming\Python\Python311\Scripts)
2) poetry new pe-orgair-platform
cd pe-orgair-platform
poetry env info
poetry config virtualenvs.in-project true
poetry install

-- Install dependencies
# Install Week 1 dependencies
poetry add fastapi "uvicorn[standard]" pydantic pydantic-settings httpx
poetry add snowflake-connector-python sqlalchemy alembic boto3 redis
poetry add structlog sse-starlette websockets
# Development dependencies
poetry add --group dev pytest pytest-asyncio pytest-cov black ruff mypy hypothesis

-- fast api
poetry add fastapi uvicorn
