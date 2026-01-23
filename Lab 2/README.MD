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