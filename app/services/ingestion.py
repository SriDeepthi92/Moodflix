import pandas as pd

from app.db.database import SessionLocal
from app.db.models import Show
from app.services.embeddings import generate_embedding


def ingest_shows():
    db = SessionLocal()

    df = pd.read_csv("data/shows.csv")

    for _, row in df.iterrows():

        embedding = generate_embedding(row["overview"])

        show = Show(
            title=row["title"],
            overview=row["overview"],
            embedding=embedding
        )

        db.add(show)

    db.commit()
    db.close()

    print("Data ingestion completed.")


if __name__ == "__main__":
    ingest_shows()