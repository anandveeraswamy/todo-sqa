# tests/conftest.py
import pytest
from app import create_app, db
from config import Config
from app.models import User, Todo


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    # Separate database file for tests
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


@pytest.fixture
def app():
    """Create a new app instance for each test function."""
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Flask test client for making requests."""
    return app.test_client()


@pytest.fixture
def user(app):
    """Create a simple test user in the database."""
    u = User(username="testuser")
    u.set_password("Password123!")
    db.session.add(u)
    db.session.commit()
    return u

@pytest.fixture
def todo(app, user):
    """Create a simple todo in the database."""
    t = Todo(
            title="Test task",
            description="Test description",
            user=user
        )
    db.session.add(t)
    db.session.commit()
    return t


class AuthActions:
    """Small helper to log in and out in tests."""

    def __init__(self, client):
        self._client = client

    def login(self, username="testuser", password="Password123!"):
        return self._client.post(
            "/login",
            data={"username": username, "password": password},
            follow_redirects=True,
        )

    def logout(self):
        return self._client.get("/logout", follow_redirects=True)


@pytest.fixture
def auth(client, user):
    """Return an auth helper bound to the client."""
    return AuthActions(client)
