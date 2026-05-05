from services.users import get_user


def test_get_user_hits_httpbin():
    user = get_user(42)
    assert user["method"] == "GET"
    assert user["url"].endswith("/anything/users/42")
