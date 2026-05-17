# MoodFlix

Semantic movie and TV discovery engine powered by vector search and natural language understanding.

## Demo Concept

Instead of searching for exact titles:

> "something creepy but cosy for a rainy evening"

MoodFlix uses semantic embeddings and vector similarity search to discover relevant shows and movies.

## Tech Stack

- FastAPI
- PostgreSQL
- pgvector
- Docker
- Python

Later:

- sentence-transformers
- Airflow
- dbt

## Architecture

```text
User Query
    ↓
FastAPI
    ↓
Embedding Service
    ↓
pgvector Similarity Search
    ↓
PostgreSQL
```

## Run Locally

```bash
docker compose up --build
```

Then open `http://localhost:8000` and check the health endpoint at `http://localhost:8000/`.

## Roadmap

- [x] Dockerized FastAPI setup
- [x] PostgreSQL + pgvector integration
- [ ] Semantic embeddings pipeline
- [ ] Natural language recommendation engine
- [ ] TMDB ingestion pipeline
- [ ] Airflow orchestration
- [ ] dbt analytics models
- [ ] Recommendation evaluation metrics
