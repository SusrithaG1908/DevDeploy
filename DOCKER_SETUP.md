# DevDeploy Docker Setup

## Start
docker compose up --build -d

## Status
docker compose ps

## Health check
http://localhost:5000/health

## Logs
docker compose logs -f student-app

## Stop
docker compose down

The app uses Gunicorn and runs as a non-root user.
Student records are stored in memory and are not persisted across container recreation.
