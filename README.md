# FastAPI Test Assignment

This repository contains the solution for two backend tasks:

1. **Task 1** — RESTful API for managing a to-do list with FastAPI  
2. **Task 2** — automation and external API integration with Celery and Redis

## Implemented Tasks

### Task 1 — RESTful API

Implemented a simple to-do API with in-memory storage.

**Features:**
- Get all tasks
- Create a new task
- Update an existing task
- Delete a task
- Validate input data with Pydantic
- Cover API with unit tests

### Task 2 — Automation and External API Integration

Implemented a background task that:
- fetches users from a public API
- extracts `id`, `name`, and `email`
- saves the data to a CSV file
- runs asynchronously with Celery
- uses Redis as a message broker

## Tech Stack

- Python
- FastAPI
- Pydantic
- Celery
- Redis
- Docker
- Docker Compose
- Pytest

## Project Structure

```text
.
├── app/
│   ├── main.py
│   ├── services.py
│   ├── storage.py
│   ├── schemas.py
│   ├── celery_tasks.py
│   └── routers/
│       ├── tasks.py
│       └── users.py
├── tests/
│   └── test_tasks.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/igor-chernobai/fastapi-todo.git
cd fastapi-todo
```

2. **Run the project:**

```bash
docker compose up --build
```

3. **Open the application:**

- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

## API Endpoints

### Task 1 — To-do API

- `GET /tasks` — get all tasks
- `POST /tasks` — create a new task
- `PUT /tasks/{task_id}` — update a task
- `DELETE /tasks/{task_id}` — delete a task

### Task 2 — Users Import

- `POST /users/import` — start background users import

## Run Tests

Run tests inside the container:

```bash
docker compose exec app pytest -v
```

## Notes

- Tasks are stored in memory and are not persisted after application restart.
- Celery uses Redis as the message broker.
- Users are fetched from `https://jsonplaceholder.typicode.com/users`.
- Imported users are saved to a CSV file with the following fields: `id`, `name`, `email`.