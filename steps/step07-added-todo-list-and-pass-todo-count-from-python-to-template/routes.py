from app import app
from flask import render_template
from datetime import datetime

todos = [
    {
        "id": 1,
        "title": "title1",
        "description": "description1",
        "created_at": "2025-11-12 06:27:37",
    },
    {
        "id": 1,
        "title": "title1",
        "description": "description1",
        "created_at": "2025-11-12 06:27:37",
    },
    {
        "id": 1,
        "title": "title1",
        "description": "description1",
        "created_at": "2025-11-12 06:27:37",
    }
]


@app.route("/")
def index():
    todo_count = len(todos)
    return render_template("index.html", todo_count=todo_count)


@app.route("/tasks")
def all_tasks():
    return render_template("tasks.html")


@app.route("/task/<int:task_id>")
def task(task_id):
    return f"<h1>Task detail page for task {task_id}</h1>"


@app.route("/new-task")
def create_task():
    return render_template("new_task.html")
