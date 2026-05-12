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
    return hashlib.md5(long_url.encode()).hexdigest()[:8]


def base64_hash(long_url: str) -> str:
    return base64.urlsafe_b64encode(long_url.encode()).decode()[:8]


def random_string(_long_url: str) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=8))


class Counter:
    def __init__(self) -> None:
        self._counter = itertools.count(1)
        self._lock = threading.Lock()

    def __call__(self, _long_url: str) -> str:
        with self._lock:
            return str(next(self._counter))


# --- Shortener ---


class UnknownShortURLError(KeyError): ...


class CollisionError(RuntimeError): ...


class URLShortener:
    def __init__(self, strategy: Strategy | None = None) -> None:
        self._strategy: Strategy = strategy or random_string
        self._short_to_long: dict[str, str] = {}
        self._long_to_short: dict[str, str] = {}  # it's only required for idempotency
        self._lock = threading.Lock()

    def shorten(self, long_url: str) -> str:
        with self._lock:
            short_url = self._long_to_short.get(long_url)
            if short_url is not None:
                return short_url

            short_url = self._strategy(long_url)

            if self._short_to_long.get(short_url) is not None:
                raise CollisionError("Already maps to another url")

            self._long_to_short[long_url] = short_url
            self._short_to_long[short_url] = long_url
            return short_url

    def expand(self, short_url: str) -> str:
        try:
            return self._short_to_long[short_url]
        except KeyError:
            raise UnknownShortURLError(short_url)
