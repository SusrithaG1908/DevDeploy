# Docker and Docker Compose (Member 3)

This adds container support for the Flask Student Management System.

## Prerequisites

- Docker Engine/Desktop with Docker Compose v2 (`docker compose`)
- Existing project files: `app.py`, `templates/index.html`, and `requirements.txt`

## Build and start

Run these commands from the repository root (the directory containing `Dockerfile`):

```bash
docker compose up --build -d
docker compose ps
```

Open the application at <http://localhost:5000>.

## Verify

Check the health endpoint:

```bash
curl http://localhost:5000/health
```

Expected response:

```json
{"status":"healthy"}
```

Check the JSON API:

```bash
curl http://localhost:5000/api/students
```

View application logs:

```bash
docker compose logs -f student-app
```

Stop and remove the container/network:

```bash
docker compose down
```

## Design notes

- `Dockerfile` builds a reproducible image from Python 3.12 slim.
- `gunicorn` serves Flask as a WSGI application; the Flask development server is not used in the container.
- The container runs as a non-root user.
- Compose maps host port 5000 to container port 5000, restarts the service unless explicitly stopped, and checks `/health`.
- `.dockerignore` prevents Git metadata, virtual environments, caches, and local environment files from entering the build context.
- **Data limitation:** the current application stores students in a Python in-memory list. Changes are lost when the container is recreated or restarted. Persistent storage/database work is outside this Docker-only task.

## Suggested Git workflow

```bash
git checkout develop
git pull origin develop
git checkout -b feature/docker
# Copy the Dockerfile, docker-compose.yml, .dockerignore, and DOCKER_SETUP.md into the repo root.
git add Dockerfile docker-compose.yml .dockerignore DOCKER_SETUP.md
git commit -m "chore: containerize Flask app with Docker Compose"
git push -u origin feature/docker
```

Then open a pull request from `feature/docker` into `develop`, as specified in `CONTRIBUTING.md`.
