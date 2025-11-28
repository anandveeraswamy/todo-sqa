from app import app, db
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from forms import LoginForm, RegistrationForm
from models import User, Todo
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask import request
from urllib.parse import urlsplit


@app.route("/")
@login_required
def index():    
    todo_count = Todo.query.count()
    return render_template("index.html", todo_count=todo_count)


@app.route("/tasks")
@login_required
def all_tasks():
    todos = Todo.query.all()
    return render_template("tasks.html", todos=todos)


@app.route("/task/<int:task_id>")
@login_required
def task(task_id):  
    task = Todo.query.get_or_404(task_id)
    return render_template("task.html", task=task)


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):    
    task = Todo.query.get_or_404(task_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")        
        task.title = title
        task.description = description
        db.session.commit()
        return redirect(url_for("task", task_id=task_id))
    return render_template("task_form.html", task=task)


@app.route("/new-task", methods=["GET", "POST"])
@login_required
def create_task():
    if request.method == "POST":        
        title = request.form.get("title")
        description = request.form.get("description")        
        task = Todo(
            title=title,
            description=description,
            user=current_user, 
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("task", task_id=task.id))
    return render_template("task_form.html", task=None)


@app.route("/delete-task/<int:task_id>", methods=["Post"])
@login_required
def delete_task(task_id):
    task = Todo.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("all_tasks"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.get_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")        
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, your registration was successful")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)
