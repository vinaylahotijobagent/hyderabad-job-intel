import sqlite3

DB_NAME = "jobs.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            job_id TEXT PRIMARY KEY,
            company TEXT,
            title TEXT,
            link TEXT,
            search_term TEXT,
            posted_ts INTEGER,
            processed INTEGER DEFAULT 0,
            date_seen TEXT
        )
    """)

    conn.commit()
    conn.close()
