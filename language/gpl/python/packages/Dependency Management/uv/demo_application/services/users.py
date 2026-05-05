import requests

from config import API_BASE_URL, TIMEOUT


def get_user(user_id: int) -> dict:
    response = requests.get(
        f"{API_BASE_URL}/anything/users/{user_id}",
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    return response.json()
