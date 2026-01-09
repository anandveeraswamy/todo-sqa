from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Todo

bp = Blueprint("tasks", __name__)


@bp.route("/tasks")
@login_required
def all_tasks():
    todos = Todo.query.all()
    return render_template("tasks.html", todos=todos)


@bp.route("/task/<int:task_id>")
@login_required
def task(task_id):
    task = db.session.get(Todo, task_id)
    return render_template("task.html", task=task)


@bp.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = db.session.get(Todo, task_id)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        task.title = title
        task.description = description
        db.session.commit()
        return redirect(url_for("tasks.task", task_id=task_id))
    return render_template("task_form.html", task=task)


@bp.route("/new-task", methods=["GET", "POST"])
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
        return redirect(url_for("tasks.task", task_id=task.id))
    return render_template("task_form.html", task=None)


@bp.route("/delete-task/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    task = db.session.get(Todo, task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks.all_tasks"))


@bp.route("/task/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle_task_completion(task_id):
    task = db.session.get(Todo, task_id)
    task.completed = not task.completed
    db.session.commit()

    if task.completed:
        flash(f"Task {task.title} marked as completed.")
    else:
        flash(f"Task {task.title} reopened.")
    return redirect(url_for("tasks.all_tasks"))
