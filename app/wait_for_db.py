import time
import psycopg2
import os


while True:
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("POSTGRES_PORT"),
        )

        conn.close()

        print("PostgreSQL is ready!")
        break

    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(2)