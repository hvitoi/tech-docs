import base64
import hashlib
import itertools
import random
import string
import threading
from collections.abc import Callable

# --- Strategies ---


type Strategy = Callable[[str], str]


def md5_hash(long_url: str) -> str:
    """First 8 hex chars of MD5(long_url). Deterministic — same input → same output."""
    return hashlib.md5(long_url.encode()).hexdigest()[:8]


def base64_hash(long_url: str) -> str:
    """First 8 chars of urlsafe-base64(long_url). Deterministic."""
    return base64.urlsafe_b64encode(long_url.encode()).decode()[:8]


def random_string(_long_url: str) -> str:
    """8 random alphanumeric chars. Non-deterministic — ignores long_url."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=8))


class Counter:
    """Monotonic incrementing identifier — ignores long_url, just hands out the next int.

    The lock guards the read-modify-write of the underlying counter against
    lost updates when multiple threads call __call__ concurrently.
    """

    def __init__(self) -> None:
        self._counter = itertools.count(1)
        self._lock = threading.Lock()

    def __call__(self, _long_url: str) -> str:
        with self._lock:
            return str(next(self._counter))


# --- Shortener ---


class UnknownShortURLError(KeyError):
    pass


class CollisionError(RuntimeError):
    pass


class URLShortener:
    def __init__(self, strategy: Strategy | None = None) -> None:
        self._strategy: Strategy = strategy or Counter()
        self._long_to_short: dict[str, str] = {}
        self._short_to_long: dict[str, str] = {}
        self._lock = threading.Lock()

    def shorten(self, long_url: str) -> str:
        with self._lock:
            short_url = self._long_to_short.get(long_url)
            if short_url is not None:
                return short_url

            short_url = self._strategy(long_url)

            if self._short_to_long.get(short_url) is not None:
                raise CollisionError(f"{short_url!r} already maps to another url")

            self._long_to_short[long_url] = short_url
            self._short_to_long[short_url] = long_url
            return short_url

    def expand(self, short_url: str) -> str:
        try:
            return self._short_to_long[short_url]
        except KeyError:
            raise UnknownShortURLError(short_url)
