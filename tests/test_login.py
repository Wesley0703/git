from app.login import login

def test_login_success():
    assert login("admin", "1234") is True

def test_login_fail_wrong_password():
    assert login("admin", "wrong") is False

def test_login_fail_wrong_user():
    assert login("user", "1234") is False
