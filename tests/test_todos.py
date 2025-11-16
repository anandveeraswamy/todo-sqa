# tests/test_todos.py
from app import db
from app.models import Todo


def test_tasks_requires_login(client):
    resp = client.get("/tasks", follow_redirects=False)
    assert resp.status_code in (301, 302)
    assert "/login" in resp.headers["Location"]


def test_tasks_page_lists_todos(app, client, auth, user):
    # Create some todos directly in the db
    t1 = Todo(title="Task 1", description="Desc 1", user=user)
    t2 = Todo(title="Task 2", description="Desc 2", user=user)
    db.session.add_all([t1, t2])
    db.session.commit()

    auth.login()
    resp = client.get("/tasks")

    # assert resp.status_code == 200
    assert b"Task 1" in resp.data
    assert b"Task 2" in resp.data


def test_create_task_via_form(client, auth):
    auth.login()

    resp = client.post(
        "/new-task",
        data={"title": "Form task", "description": "From form"},
        follow_redirects=True,
    )
    assert resp.status_code == 200

    # Check that it actually exists in the database
    from app.models import Todo  # imported here to keep top imports simple
    from app import db

    created = db.session.query(Todo).filter_by(title="Form task").first()
    assert created is not None
    assert created.description == "From form"
