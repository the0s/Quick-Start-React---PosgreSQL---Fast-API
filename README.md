# Quick starter FastAPI - React - PostgreSQL

Make sure docker is running!
- FastAPI for backend 
- Connects to the postgresql through sqlalchemy ORM
- React Frontend to display resutls


## Build (Local) 
docker-compose -f docker-compose.yml build

## Run (Local) 
docker-compose -f docker-compose.yml up 

## For First Time and 
### On another Terminal Run this to create the schema for SQL database
docker-compose -f docker-compose.yml exec server alembic upgrade head
### Go Here to populate the database with the raw-data
http://127.0.0.1:8000/populate/

## Access the app here:
Frontend: http://127.0.0.1:3000/

Backend: http://127.0.0.1:8000/medals/2004

Backend Docs: http://127.0.0.1:8000/docs

## Run the Tests
docker-compose -f docker-compose.yml exec server pytest

