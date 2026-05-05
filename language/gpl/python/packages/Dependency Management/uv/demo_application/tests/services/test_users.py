from services.users import get_user


def test_get_user_hits_httpbin(user_id):
    user = get_user(user_id)
    assert user["method"] == "GET"
    assert user["url"].endswith(f"/anything/users/{user_id}")
