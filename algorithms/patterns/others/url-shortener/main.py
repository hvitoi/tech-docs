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
        self.counter = itertools.count(1)
        self._lock = threading.Lock()

    def __call__(self, _long_url: str) -> str:
        with self._lock:
            return str(next(self.counter))


# --- Shortener ---


class UnknownShortURLError(KeyError): ...


class CollisionError(RuntimeError): ...


class URLShortener:
    def __init__(self, strategy: Strategy | None = None) -> None:
        self.strategy: Strategy = strategy or random_string
        self.short_to_long: dict[str, str] = {}
        self.long_to_short: dict[str, str] = {}  # it's only required for idempotency
        self._lock = threading.Lock()

    def shorten(self, long_url: str) -> str:
        with self._lock:
            if long_url in self.long_to_short:
                return self.long_to_short[long_url]

            short_url = self.strategy(long_url)

            if short_url in self.short_to_long:
                raise CollisionError("Already maps to another url")

            self.long_to_short[long_url] = short_url
            self.short_to_long[short_url] = long_url
            return short_url

    def expand(self, short_url: str) -> str:
        if short_url not in self.short_to_long:
            raise UnknownShortURLError(short_url)
        return self.short_to_long[short_url]
