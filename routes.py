from app import app, db
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from forms import LoginForm
from models import User, Todo
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask import request
from urllib.parse import urlsplit

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
@login_required
def index():
    todo_count = len(todos)
    return render_template("index.html", todo_count=todo_count)


@app.route("/tasks")
@login_required
def all_tasks():    
    return render_template("tasks.html", todos=todos)


@app.route("/task/<int:task_id>")
@login_required
def task(task_id):
    # index = task_id - 1
    # task = todos[index]
    task = None
    for todo in todos:
        if todo["id"] == task_id:
            task = todo
    return render_template("task.html", task=task)    


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
@login_required
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
@login_required
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
@login_required
def delete_task(task_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != task_id]
    return redirect(url_for("all_tasks"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))    
    form = LoginForm()    
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)            
        )
        if user is None or not user.get_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for(login))
        login_user(user, remember=form.remember_me.data)      
        next_page = request.args.get('next')
        # To determine if the URL is absolute or relative, 
        # I parse it with Python's urlsplit() function and then 
        # check if the netloc component is set or not.
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)      
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
