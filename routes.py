from app import app
from flask import render_template, request, redirect, url_for
from datetime import datetime

todos = [
    {
        "id": 1,
        "title": "Set up Flask Project Structure",
        "description": "Create the Flask application, configure routes, and establish the basic folder structure for templates, static files, and modules.",
        "created_at": "2025-12-01 09:42:17",
    },
    {
        "id": 2,
        "title": "Design Blog Post Model",
        "description": "Define the database schema for blog posts, including title, content, author, and timestamp fields, using SQLAlchemy or an equivalent ORM.",
        "created_at": "2025-12-03 15:26:49",
    },
    {
        "id": 3,
        "title": "Implement Post Creation Form",
        "description": "Add a form using Flask-WTF to allow users to create new blog posts, validate inputs, and store entries in the database.",
        "created_at": "2025-11-30 11:58:05",
    }
]



@app.route("/")
def index():
    todo_count = len(todos)
    return render_template("index.html", todo_count=todo_count)


@app.route("/tasks")
def all_tasks():    
    return render_template("tasks.html", todos=todos)


@app.route("/task/<int:task_id>")
def task(task_id):
    # index = task_id - 1
    # task = todos[index]
    task = None
    for todo in todos:
        if todo["id"] == task_id:
            task = todo
    return render_template("task.html", task=task)    


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    index = task_id - 1
    task = todos[index]    
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        todos[index]["title"] = title
        todos[index]["description"] = description
        return redirect(url_for("task", task_id=task_id))
    
    return render_template("task_form.html", task=task)


@app.route("/new-task", methods=["GET", "POST"])
def create_task():    
    if request.method == "POST":
        task_id = todos[-1]["id"] + 1
        title = request.form.get("title")
        description = request.form.get("description")
        todos.append({
         "id": task_id,
         "title": title,
         "description": description ,
         "created_at": datetime.now()
        })
        return redirect(url_for("task", task_id=task_id))    
    return render_template("task_form.html", task=None)


@app.route("/delete-task/<int:task_id>", methods=["Post"])
def delete_task(task_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != task_id]
    return redirect(url_for("all_tasks"))
