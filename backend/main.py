import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

    yield # everything before yield runs at startup. Everything after runs at shutdown

app = FastAPI(
    title="Student API",
    description="API for Student CRUD operations",
    version="1.0.0",
    docs_url="/docs",
    lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Only allow your Svelte frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes

@app.get('/')
async def get_all_students():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = 'SELECT id, first_name, last_name FROM students'
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    students = [{"id": row[0], "first_name": row[1], "last_name": row[2]} for row in rows]
    return students