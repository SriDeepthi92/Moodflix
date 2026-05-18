from fastapi import FastAPI

from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="MoodFlix",
    description="Semantic TV show and movie discovery engine",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "running"}
@app.get("/root")
def root():
    return {"status": "running"}