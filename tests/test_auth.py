# tests/test_auth.py

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
    # Later you can tighten this to check actual page content
