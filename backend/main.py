import os
from fastapi import FastAPI
from contextlib import asynccontextmanager
import sqlite3

# db path
DB_PATH = "students.db"

# startup config
@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS students
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        class_level TEXT NOT NULL, 
                        graduation_year INTEGER NOT NULL
                    )
                """
        
        cur.execute(query)
        conn.commit()
        conn.close()

    yield