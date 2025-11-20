# tests/test_models.py
from app import db
from app.models import User, Todo


def test_user_password_hashing(app):
    user = User(username="alice")
    user.set_password("secret123")

    db.session.add(user)
    db.session.commit()

    assert user.password_hash is not None
    assert user.get_password("secret123") is True
    assert user.get_password("wrong") is False


def test_todo_belongs_to_user(app, user):
    todo = Todo(
        title="Test task",
        description="Description here",
        user=user,
    )
    db.session.add(todo)
    db.session.commit()

    assert todo.id is not None
    assert todo.user_id == user.id
    assert todo.user.username == "testuser"


def test_todo_has_completed_flag_defaults_false(app, user):
    todo = Todo(
        title="Test task",
        description="Description here",
        user=user,
    )
    db.session.add(todo)
    db.session.commit()

    assert todo.completed is False

