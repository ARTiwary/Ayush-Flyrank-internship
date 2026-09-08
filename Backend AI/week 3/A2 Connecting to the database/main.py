from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3

app = FastAPI(title="Task SQLite API", version="2.0")

DB_FILE = "tasks.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Allows dictionary-like access to rows
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Stage 0: Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    """)
    
    # Check if table is empty to insert initial 3 tasks
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]
    if count == 0:
        initial_tasks = [
            ("Learn FastAPI fundamentals", 0),
            ("Build a complete CRUD API", 0),
            ("Push project to GitHub", 1)
        ]
        cursor.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", initial_tasks)
        conn.commit()
        
    conn.close()

# Initialize database on startup
init_db()

# Pydantic models for validation
class TaskCreate(BaseModel):
    title: str
    done: Optional[bool] = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


# Stage 1: Root and Health Endpoints
@app.get("/")
def read_root():
    return {
        "name": "Task SQLite API",
        "version": "2.0",
        "endpoints": ["/tasks", "/health", "/docs"]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}


# Stage 1: Read Endpoints from SQLite
@app.get("/tasks")
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    
    return [{"id": row["id"], "title": row["title"], "done": bool(row["done"])} for row in rows]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
        
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}


# Stage 2: Create Endpoint (INSERT into SQLite)
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    if not task_data.title or not task_data.title.strip():
        raise HTTPException(status_code=400, detail={"error": "Title is required and cannot be empty"})
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task_data.title.strip(), 1 if task_data.done else 0)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return {"id": new_id, "title": task_data.title.strip(), "done": bool(task_data.done)}


# Stage 3: Update and Delete Endpoints (SQL Update & Delete)
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if task exists
    cursor.execute("SELECT id, title, done FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    
    current_title = row["title"]
    current_done = row["done"]
    
    if task_data.title is not None:
        if not task_data.title.strip():
            conn.close()
            raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
        current_title = task_data.title.strip()
        
    if task_data.done is not None:
        current_done = 1 if task_data.done else 0
        
    cursor.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (current_title, current_done, task_id)
    )
    conn.commit()
    conn.close()
    
    return {"id": task_id, "title": current_title, "done": bool(current_done)}

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
        
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    
    return None