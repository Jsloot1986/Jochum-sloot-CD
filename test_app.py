from app import index, user

def test_index():
    assert index() == "Hello, world!"

def test_user():
    assert user() == "Hello, Jochum!"