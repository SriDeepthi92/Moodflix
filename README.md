# MoodFlix

MoodFlix is a semantic TV show and movie discovery engine powered by vector search and natural language understanding.

Instead of searching by exact titles, users can describe a mood, atmosphere, or feeling:

> "something creepy but cosy for a rainy evening"

MoodFlix converts natural language into vector embeddings and retrieves semantically similar shows using PostgreSQL + pgvector.

---

# Current Status

## Implemented

- Dockerized development environment
- FastAPI backend
- PostgreSQL database
- pgvector integration
- SQLAlchemy setup
- Embedding service architecture
- Semantic search foundation

## In Progress

- CSV ingestion pipeline
- Embedding generation
- Vector similarity search endpoint

---

# Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy
- sentence-transformers
- Docker & Docker Compose

---

# Project Architecture

```text
User Query
    ↓
FastAPI API Layer
    ↓
Embedding Service
    ↓
pgvector Similarity Search
    ↓
PostgreSQL
```

# Project Structure

```text
moodflix/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │
│   ├── core/
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── services/
│   │   ├── embeddings.py
│   │   ├── ingestion.py
│   │   └── search.py
│   │
│   ├── schemas/
│   │
│   └── main.py
│
├── data/
├── tests/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

# Local Development

Start Containers

```bash
docker compose up --build
```

Stop Containers

```bash
docker compose down
```

Restart Containers

```bash
docker compose restart
```

## API Documentation

FastAPI automatically generates Swagger documentation:

http://localhost:8000/docs

## Database

MoodFlix uses PostgreSQL with the pgvector extension for vector similarity search.

Example vector-enabled table:

```sql
CREATE TABLE shows (
    id SERIAL PRIMARY KEY,
    title TEXT,
    overview TEXT,
    embedding VECTOR(384)
);
```

## Semantic Search

MoodFlix uses sentence-transformer embeddings to represent show descriptions and user queries as high-dimensional vectors.

Example query:

"dark rainy psychological mystery"

Expected semantic matches:

- Dark
- Mindhunter
- Stranger Things
- Roadmap

## Roadmap

### Backend & Retrieval

- Dockerized FastAPI setup
- PostgreSQL + pgvector integration
- Embedding service structure
- CSV ingestion pipeline
- Semantic similarity search
- Search API endpoint
- Async ingestion tasks

### Data Engineering

- TMDB ingestion pipeline
- Airflow orchestration
- dbt transformations
- Recommendation analytics models

### Product Features

- Mood-based recommendations
- Genre clustering
- Similar show recommendations
- User watch history
- Recommendation evaluation metrics

## Vision

MoodFlix explores a different way of discovering entertainment — searching by emotional intent rather than exact titles or genres.

The project combines:

- backend engineering
- vector databases
- semantic retrieval systems
- modern PostgreSQL features
- AI-powered search architecture

into a production-oriented learning project.
