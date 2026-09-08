from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0")

# In-memory storage (database simulation)
tasks = [
    {"id": 1, "title": "Learn FastAPI fundamentals", "done": False},
    {"id": 2, "title": "Build a complete CRUD API", "done": False},
    {"id": 3, "title": "Push project to GitHub", "done": True},
]

# Pydantic models for request validation
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
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks", "/health", "/docs"]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}


# Stage 2: Read Endpoints (List & Single Task with 404 Handling)
@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})
    return task


# Stage 3: Create Endpoint (POST with Validation & 201 Status)
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    if not task_data.title or not task_data.title.strip():
        raise HTTPException(status_code=400, detail={"error": "Title is required and cannot be empty"})
    
    new_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": task_data.title.strip(),
        "done": task_data.done if task_data.done is not None else False
    }
    tasks.append(new_task)
    return new_task


# Stage 4: Update & Delete Endpoints (PUT & DELETE)
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})
    
    if task_data.title is not None:
        if not task_data.title.strip():
            raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
        task["title"] = task_data.title.strip()
        
    if task_data.done is not None:
        task["done"] = task_data.done
        
    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail={"error": f"Task {task_id} not found"})
    
    tasks = [t for t in tasks if t["id"] != task_id]
    return None