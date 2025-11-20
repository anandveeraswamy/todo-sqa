from app import db
from app.models import Todo


def test_tasks_requires_login(client):
    resp = client.get("/tasks", follow_redirects=False)
    assert resp.status_code in (301, 302)
    assert "/login" in resp.headers["Location"]

def test_index_shows_todo_count(app, client, auth, user):
    """ checks if the correct template with the correct data is called """
    auth.login()
    
    t1 = Todo(title="Task 1", description="Desc 1", user=user)
    t2 = Todo(title="Task 2", description="Desc 2", user=user)
    db.session.add_all([t1, t2])
    db.session.commit()

    response = client.get("/")

    assert response.status_code == 200
    # Adjust string to match whatever is in index.html
    assert b"You have 2 tasks in total" in response.data

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
    
    resp = client.get("/new-task")
    assert resp.status_code == 200

    resp = client.post(
        "/new-task",
        data={"title": "Form task", "description": "From form"},
        follow_redirects=True,
    )
    assert resp.status_code == 200

    # Check that it actually exists in the database
    created = db.session.query(Todo).filter_by(title="Form task").first()
    assert created is not None
    assert created.description == "From form"
    
def test_edit_task_via_form(client, auth):
    auth.login()
    
    new_task_response = client.post(
        "/new-task",
        data={"title": "title1", "description": "desc1"},
        follow_redirects=True,
    )
    assert new_task_response.status_code == 200
    
    get_edit_response = client.get('/edit-task/1')
    assert get_edit_response.status_code == 200
    
    post_edit_response = client.post(
        "/edit-task/1",
        data={"title": "title1-edited", "description": "desc1-edited"},
        follow_redirects=True
    )
    
    assert post_edit_response.status_code == 200
    created = db.session.query(Todo).filter_by(title="title1-edited").first()
    assert created is not None
    assert created.description == "desc1-edited"    
    
    
def test_delete_task_via_form(client, auth):
    auth.login()
    
    new_task_response = client.post(
        "/new-task",
        data={"title": "title1", "description": "desc1"},
        follow_redirects=True,
    )
    assert new_task_response.status_code == 200
    created = db.session.query(Todo).filter_by(title="title1").first()
    assert created is not None
    assert created.description == "desc1"    
    
    delete_task_response = client.post(
        "/delete-task/1",
        follow_redirects=True
    )
    assert delete_task_response.status_code == 200
    deleted = db.session.query(Todo).filter_by(title="title1").first()
    assert deleted is None
    
def test_login_authenticated_user(client, auth):
    """ Already authenticated user should be taken to the index page """
    auth.login()
    
    authenticated_user_response = client.get("/login", follow_redirects=True)
    assert authenticated_user_response.status_code == 200
    assert b"Hello Testuser" in authenticated_user_response.data 

def test_mark_task_complete(client, auth, user):
    auth.login()  
    todo = Todo(
        title="Test task",
        description="Description here",
        user=user,
    )
    db.session.add(todo)
    db.session.commit()
    todo_id = todo.id

    resp = client.post(
        f'/task/{todo_id}/complete',
        follow_redirects=True
    )

    assert resp.status_code == 200
    updated = db.session.get(Todo, todo_id)
    assert updated.completed is True