# FastAPI Test Assignment

This repository contains a solution for three backend tasks and demonstrates a modular, scalable approach to Python backend development.

## Tasks Overview

1. **Task 1** — RESTful API for managing a to-do list with FastAPI.
2. **Task 2** — Automation and external API integration with Celery and Redis.
3. **Task 3** — Machine Learning integration for task priority classification.

## Implemented Tasks

### Task 1 — RESTful API
A robust to-do API with in-memory storage and validation.

**Features:**
- CRUD operations for tasks
- Pydantic data validation
- Unit test coverage with Pytest

### Task 2 — Automation & Celery
An asynchronous background service for data processing.

**Workflow:**
- Fetches users from a public API
- Extracts `id`, `name`, and `email`
- Saves the result to a CSV file

**Tech used:**
- **Celery** as the task runner
- **Redis** as the message broker

### Task 3 — Machine Learning Integration

A predictive service that automatically classifies task priorities based on task descriptions.

**Model:**
- A Scikit-learn pipeline with **TfidfVectorizer** and **LogisticRegression**
- Trained on a custom CSV dataset for text-based priority classification

**Integration:**
- The trained model is serialized and stored as a `joblib` file
- The FastAPI application loads the model and uses it for real-time inference

## Tech Stack & Tools

- **Core:** Python, FastAPI, Pydantic
- **Async processing:** Celery, Redis
- **Machine Learning:** Scikit-learn, Pandas, Joblib
- **Testing:** Pytest
- **Infrastructure:** Docker, Docker Compose
- **Code Quality:** Flake8, Isort

## Project Structure

```text
.
├── app/
│   ├── main.py             # Application entry point
│   ├── services/           # Business logic and ML predictor
│   ├── storage.py          # In-memory data storage
│   ├── schemas.py          # Pydantic schemas
│   ├── celery_tasks.py     # Celery worker and tasks
│   └── routers/            # API routes (tasks, users, ml)
├── ml/
│   ├── train_model.py      # Model training script
│   ├── task_model.joblib   # Trained model
│   └── train.csv           # Training dataset
├── tests/                  # Pytest test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .flake8                 # Flake8 configuration
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/igor-chernobai/fastapi-todo.git
cd fastapi-todo
```

### 2. Start the project with Docker

```bash
docker-compose up --build
```

### 3. Open the API documentation

Swagger UI:

```text
http://localhost:8000/docs
```

You can use Swagger UI to test all available endpoints interactively.

## API Endpoints

### Tasks

- `GET /tasks` — List all tasks
- `POST /tasks` — Create a new task *(priority is automatically predicted via ML)*
- `PUT /tasks/{id}` — Update an existing task
- `DELETE /tasks/{id}` — Delete a task

### Users Import (Celery)

- `POST /users/import` — Trigger background CSV export of users

### ML Integration

- `POST /ml/predict` - Predict task priority based on task description

## Quality Control & Tests

### Run unit tests

```bash
docker-compose exec app pytest -v
```

## Notes

- Task data is stored in memory, so it will be reset after each application restart.
- Redis is used as the message broker for Celery background tasks.
- User data is retrieved from the public API `https://jsonplaceholder.typicode.com/users`.
- Exported CSV files include the following fields: `id`, `name`, and `email`.
- The ML model is trained on a custom CSV dataset and used to predict task priority based on task description.
- The trained model is saved as a `joblib` file and loaded by the API for inference.

## Summary

This project demonstrates:
- REST API development with FastAPI
- Background task processing with Celery and Redis
- Basic ML integration into a backend service
- Testing and code quality practices
- Containerized application setup with Docker