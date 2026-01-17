- pip install poetry
- add to envirornmental variables path (C:\Users\bhavy\AppData\Roaming\Python\Python311\Scripts)
- poetry new pe-orgair-platform
- cd pe-orgair-platform
- poetry env info
- poetry config virtualenvs.in-project true
- poetry install

# Install Week 1 dependencies
- poetry add fastapi "uvicorn[standard]" pydantic pydantic-settings httpx
- poetry add snowflake-connector-python sqlalchemy alembic boto3 redis
- poetry add structlog sse-starlette websockets
# Development dependencies
- poetry add --group dev pytest pytest-asyncio pytest-cov black ruff mypy hypothesis

### fast api
- poetry add fastapi uvicorn
 
- poetry run uvicorn pe_orgair.api.main:app --reload

### env activate
poetry env activate

& "C:\Users\bhavy\OneDrive\Desktop\GITHUB\BHAVYA\Big-Data-Labs\Lab 1\pe-orgair-platform\.venv\Scripts\activate.ps1"

##
- uvicorn pe_orgair.api.main:app --reload
- fast api end points
http://127.0.0.1:8000/docs


- add api end point for post greet
- and enter the age and string and get the ouptut
 - write other api end points as well
- add items.py in models
- and add end points in main.py like get,post, put, delete

- poetry add streamlit
- add scripts/app.py and add the code for streamlit
- streamlit run .\scripts\app.py