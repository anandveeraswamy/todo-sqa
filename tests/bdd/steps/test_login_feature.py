from pytest_bdd import scenarios, scenario, given, when, then
from app.models import User
from app import db

scenarios('../features/login.feature')

@given('a registered user exists')
def registered_user(auth):
    # The fixture creates the test user automatically.
    # No code is needed here.
    pass
    

@given('I am on the login page')
def on_login_page(client):    
    resp = client.get("/login")
    assert resp.status_code == 200

@when('I enter valid credentials', target_fixture="login_response")
def enter_valid_credentials(client):
    resp = client.post(
        '/login',
        data= {"username": "testuser", "password": "Password123!"},
        follow_redirects = True
    )
    return resp
    

@then('I should be redirected to the homepage')
def redirected_homepage(client, login_response):
    assert login_response.status_code == 200
    assert b'Hello Testuser' in login_response.data