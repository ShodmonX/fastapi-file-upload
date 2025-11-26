# FastAPI File Upload

A modern, asynchronous, and production-ready **FastAPI File Upload** built
with FastAPI.
Features include Docker, Alembic migrations, Pytest (85%+ coverage),
and GitHub Actions CI.

![Tests](https://github.com/ShodmonX/fastapi-file-upload/workflows/Tests/badge.svg)
![Coverage](https://codecov.io/gh/ShodmonX/fastapi-file-upload/branch/main/graph/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)

## 🚀 Features

-   Fully async **FastAPI** backend
-   **FastAPI Background Tasks** for thumbnail generation
-   **PostgreSQL** with SQLAlchemy 2.0 (async)
-   **Pydantic v2** schemas
-   **Alembic** for database migrations
-   **Docker** & docker-compose (development + production)
-   **Pytest** with 80%+ coverage (async tests)
-   **GitHub Actions** CI integration

## 🛠 Tech Stack

-   FastAPI
-   PostgreSQL + asyncpg
-   SQLAlchemy 2.0 (async)
-   Alembic
-   Pydantic-settings
-   Docker / docker-compose
-   Pytest + httpx
-   GitHub Actions

## ⚡ Quick Start (Recommended: Docker)

``` bash
git clone https://github.com/ShodmonX/fastapi-file-upload.git
cd fastapi-file-upload
cp .env.example .env
docker compose up --build -d
docker compose exec web alembic upgrade head
```

## Background Tasks

For every uploaded image, a background task generates a 200x200 px 
thumbnail and updates the status in the database.

## Project Structure
``` bash
.
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── a2c648c77b33_initial_revision.py
│       ├── bd54aa8ce1ee_add_column_files_process.py
├── alembic.ini
├── app
│   ├── core
│   │   ├── config.py
│   │   └── security.py
│   ├── crud
│   │   ├── file.py
│   ├── db
│   │   ├── base.py
│   │   └── session.py
│   ├── main.py
│   ├── models
│   │   ├── file.py
│   ├── routers
│   │   └── upload.py
│   ├── schemas
│   └── utils
│       ├── file_tasks.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    ├── test_crud.py
    ├── test_endpoint.py
    └── test_files
```

### URLs

-   API Root: http://localhost:8080
-   Swagger UI: http://localhost:8080/docs
-   Health Check: http://localhost:8080/health

## 🔧 Manual Setup (Without Docker)

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## 🔐 Environment Variables (.env)

    API_NAME=FILE UPLOAD
    API_VERSION=0.1.0
    DEBUG=1
    DATABASE_URL=postgresql+asyncpg://admin:Shodmon123@db:5432/fileupload

## API Endpoints

| Method | Endpoint                     | Description            |
|--------|------------------------------|------------------------|
| POST   | `/upload/`                   | Upload file            |
| GET    | `/upload/files/{file_hash}/` | Get file info          |
| GET    | `/health`                    | Health check           |

## 🧪 Testing

``` bash
pytest
pytest --cov=app
```

## 👨‍💻 Author

ShodmonX -- 2025
GitHub: https://github.com/ShodmonX
LinkedIn: https://www.linkedin.com/in/shodmonx/
Email: shodmonxolmurodov@gmail.com

## ✨ Contributing

Contributions are welcome!

## 📜 License

[MIT License](LICENCE)