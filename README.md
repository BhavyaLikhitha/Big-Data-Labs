# Big Data Labs

## Lab 1 Summary 
**Focus:** Project setup & basic API

- Set up **Poetry** for Python dependency and virtual environment management
- Built a **FastAPI** backend with CRUD endpoints:
  - `GET`, `POST`, `PUT`, `DELETE`
- Created **Pydantic models** for request/response validation
- Added a **Streamlit frontend** for basic UI interaction and prototyping

---

## Lab 2 Summary 
**Focus:** Data infrastructure & caching

- Used **Docker Compose** to orchestrate multiple containers
- Integrated **PostgreSQL** as the primary database
- Implemented **Alembic** for database migrations  
  *(schema version control and change tracking)*
- Added **Redis** for caching  
  *(observed faster response times on cached API requests)*

### Visual: How Lab 2 Works

Request → FastAPI → Check Redis Cache
                         ↓
              Cache Hit? → Return fast!
              Cache Miss? → Query PostgreSQL → Store in Redis → Return

--- 
