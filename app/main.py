from fastapi import FastAPI

app = FastAPI(
    title="MoodFlix",
    description="Semantic TV show and movie discovery engine",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "running"}