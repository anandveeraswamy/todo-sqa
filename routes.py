from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def all_tasks():
    return "<h1>List of all tasks</h1>"

@app.route("/task/<int:task_id>")
def task(task_id):
    return f"<h1>Task detail page for task {task_id}</h1>"

@app.route("/new-task")
def create_task():
    return f"<h1>Placeholder for creating a new task"
