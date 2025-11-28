from app import db
from app.models import User


def test_login_page_loads(client):
    resp = client.get("/login")
    assert resp.status_code == 200
    assert b"Login" in resp.data or b"Sign In" in resp.data


def test_index_requires_login(client):
    resp = client.get("/", follow_redirects=False)
    assert resp.status_code in (301, 302)
    assert "/login" in resp.headers["Location"]


def test_login_with_valid_credentials(auth):
    resp = auth.login()
    assert resp.status_code == 200


def test_login_with_invalid_credentials(client, auth):
    """invalid login credentials"""
    resp = client.post(
        "/login",
        data={"username": "anand", "password": "password"},
        follow_redirects=True,
    )

    assert b"Invalid username or password" in resp.data


def test_logout(client, auth):
    """test logout"""
    auth.login()
    resp = client.get("/logout", follow_redirects=True)
    assert b"Sign In" in resp.data


def test_authenticated_register(client, auth):
    """If the user is already logged in, then redirect to index"""
    auth.login()
    resp = client.get("/register", follow_redirects=True)
    assert b"Hello Testuser" in resp.data


def test_register(client):
    """Test new user registration"""
    username = "test_user"
    password = "password"
    resp = client.post(
        "/register",
        data={"username": username, "password": password, "password2": password},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    user = db.session.query(User).filter_by(username=username).first()
    assert user is not None
    assert user.username == username
    assert user.password_hash is not None


def test_register_get(client):
    resp = client.get("/register")
    assert resp.status_code == 200
    assert b"Register" in resp.data
