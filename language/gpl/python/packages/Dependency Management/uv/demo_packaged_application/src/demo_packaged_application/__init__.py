from .config import API_BASE_URL
from .services.users import get_user


def main() -> None:
    print(f"Using API: {API_BASE_URL}")
    user = get_user(42)
    print(f"Fetched: {user['url']}")
