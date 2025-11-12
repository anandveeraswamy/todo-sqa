from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks")
def all_tasks():
    return render_template("tasks.html")

@app.route("/task/<int:task_id>")
def task(task_id):
    return f"<h1>Task detail page for task {task_id}</h1>"

@app.route("/new-task")
def create_task():
     return render_template("new_task.html")
