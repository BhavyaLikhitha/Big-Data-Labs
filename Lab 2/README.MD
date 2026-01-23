this lab is more about
- Docker
- docker build -t fastapi-lab:1.0
- docker image
- docker ps

- docker run -d --name fastapi -p 8000:8000 fastapi-lab:1.0
- we define the port in the dockerfile


- docker start
- docker-compose up -d
- docker exec -ti pe_org_postgres psql -U pe_Admin -d pe_orgair_db 

- poetry add alembic
- ./.env\scripts\activate

- alemebic init migrations

- alembic revision -m "create sample table"


- alembic upgrade head

- alembic downgrade -1

-alembic revision -m "dataseeding"
- create a endpoint to hit a paarituclar table
and observe 


### how am i doing this lab:
- first copy paste the previous lab such that all installations are in place, building on top of lab 1
- add docker compose yml file
- and then start docker desktop and run "docker-compose up -d"
- then write "poetry add alembic"
- activate "venv" by - "& "C:\Users\bhavy\OneDrive\Desktop\GITHUB\BHAVYA\Big-Data-Labs\Lab 2\pe-orgair-platform\.venv\Scripts\activate.ps1" or " .\.venv\Scripts\activate"
- alembic init migrations