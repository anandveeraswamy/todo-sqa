from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Todo

bp = Blueprint("main", __name__)


@bp.route("/")
@login_required
def index():
    todo_count = Todo.query.count()
    return render_template("index.html", todo_count=todo_count)
