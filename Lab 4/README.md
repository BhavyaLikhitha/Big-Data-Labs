### Lab 2: Unified Data Architecture & Caching Lab

#### Alembic
#### Redis
#### Postgress
#### Docker

this lab is more about
- Docker
- docker build -t fastapi-lab:1.0
- docker image
- docker ps

- docker run -d --name fastapi -p 8000:8000 fastapi-lab:1.0
- we define the port in the dockerfile


- docker start
- docker-compose up -d
- docker exec -ti pe_orgair_postgres psql -U pe_admin -d pe_orgair_db 

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
- try connecting the database details in database cleint
- if error occurs then follow below
```bash 
✅ Step 1: Find what is using port 5432 (Windows)

Run PowerShell as Administrator and execute:

netstat -ano | findstr :5432
- Step 1: Identify the process (PID 6364)
Run:
tasklist | findstr 6364
You will almost certainly see one of these:

postgres.exe

pg_ctl.exe

pgadmin4.exe

com.docker.backend.exe

Step 2: Kill the process (force)

Once confirmed:

taskkill /PID 6364 /F
Verify the port is free
netstat -ano | findstr :5432

Permanent Fix (so this never happens again)

Because it’s a Windows Service, it will restart on reboot unless disabled.

Disable PostgreSQL service permanently

Press Win + R

Type:

services.msc


Find:

PostgreSQL (version number may be 14–18)

Right-click → Stop

Right-click → Properties

Set Startup type → Disabled

Apply → OK

Change docker-compose.yml
ports:
  - "5433:5432"

  Final Verification Checklist

Run:

docker ps
docker logs pe_orgair_postgres
```

- then write "poetry add alembic"
- activate "venv" by - "& "C:\Users\bhavy\OneDrive\Desktop\GITHUB\BHAVYA\Big-Data-Labs\Lab 2\pe-orgair-platform\.venv\Scripts\activate.ps1" or " .\.venv\Scripts\activate"
- alembic init migrations (created a migrations folder) which created a version folder as well (for schema changes tracking)
- in the alembic.ini file, there would be sqlalchemy.url where we need to add the "postgresql://pe_admin:pe_local_dev_123@localhost/pe_orgair_db"
- run this command "alembic revision -m "create sample table" which would create a py file 
- in the generated py file add upgrade (create table) and downgrade function for (dropping table)
- alembic upgrade base
- after  that "alembic revision -m "create base tables""
- copy paste the table creation code from stramlit
- run alembic uprade head

- fast api 
- copy the pe-orgair from lab 1 to lab 2
- add env as well from lab 1
# Install Week 1 dependencies
- poetry add fastapi "uvicorn[standard]" pydantic pydantic-settings httpx
- poetry add snowflake-connector-python sqlalchemy alembic boto3 redis
- poetry add structlog sse-starlette websockets

### fast api
- poetry add fastapi uvicorn
 
- poetry run uvicorn pe_orgair.api.main:app --reload
- uvicorn pe_orgair.api.main:app --reload

- add end points for /entries in main.py
- docker exec -ti pe_orgair_redis redis-cli then run command `set name "test"`and then run `get name` and then run `set big "data"` and then `get big  `

- and then run the api endpoints on `http://127.0.0.1:8000/docs`
- observe the cache time (processing time)
