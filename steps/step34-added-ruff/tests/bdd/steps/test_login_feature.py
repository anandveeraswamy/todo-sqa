from pytest_bdd import scenarios, given, when, then


scenarios("../features/login.feature")


@given("a registered user exists")
def registered_user(user):
    # The fixture creates the test user automatically.
    # No code is needed here.
    # Just implementing the fixture does the job
    pass


@given("I am on the login page")
def on_login_page(client):
    resp = client.get("/login")
    assert resp.status_code == 200


@when("I enter valid credentials", target_fixture="login_response")
def enter_valid_credentials(client):
    resp = client.post(
        "/login",
        data={"username": "testuser", "password": "Password123!"},
        follow_redirects=True,
    )
    return resp


@then("I should be redirected to the homepage")
def should_be_redirected_to_homepage(login_response):
    assert login_response.status_code == 200
    assert b"Hello Testuser" in login_response.data


@when("I enter an incorrect password", target_fixture="login_response")
def enter_incorrect_password(client):
    resp = client.post(
        "/login",
        data={"username": "testuser", "password": "wrong_password"},
        follow_redirects=True,
    )
    return resp


@when("I enter an incorrect username", target_fixture="login_response")
def enter_incorrect_username(client):
    resp = client.post(
        "/login",
        data={"username": "wrong_user", "password": "Password123!"},
        follow_redirects=True,
    )
    return resp


@then("I should remain on the login page")
def should_remain_on_login_page(login_response):
    assert login_response.status_code == 200
    assert b"Invalid username or password" in login_response.data


@given("I am already logged in")
def log_in(auth):
    auth.login()


@when("I try to visit the login page", target_fixture="login_response")
def open_login_page(client):
    resp = client.get("/login", follow_redirects=True)
    return resp


# @then('I should be redirected to the homepage')
# def should_be_redirected_to_homepage(login_response):
#     assert b'Hello Testuser' in login_response.data
# Note there is no need to add this 'then' since it is already defined
