from pytest_bdd import scenarios, scenario, given, when, then
from app.models import User
from app import db

scenarios('../features/login.feature')


@given('I am on the login page')
def on_login_page(client):
    resp = client.get("/login")
    assert resp.status_code == 200

@when('I enter valid credentials')
def enter_valid_credentials(client, auth):
    resp = client.post(
        '/login',
        data= {"username": "testuser", "password": "Password123!"},
        follow_redirects = True
    )
    assert b'Hello Testuser' in resp.data    
    

@then('I should be redirected to the homepage')
def redirected_homepage(client):
    resp = client.get('/', follow_redirects = True)
    assert resp.status_code == 200
    assert b'Hello Testuser' in resp.data