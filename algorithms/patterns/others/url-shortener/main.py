import base64
import hashlib
import itertools
import random
import string
import threading
from collections.abc import Callable

# --- strategies ---


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


# --- errors + shortener ---


class UnknownShortURLError(KeyError):
    """Raised when expand() is called with a short URL that was never shortened."""


class CollisionError(RuntimeError):
    """Raised when a generated short URL already maps to a different long URL."""


class URLShortener:
    """Bidirectional long↔short URL mapper with a pluggable generation strategy.

    `shorten` is idempotent: the same long URL always returns the same short.
    The strategy is responsible for *how* the short URL is generated; the
    shortener owns the storage and detects collisions (same short bound to a
    different long URL).
    """

    def __init__(self, strategy: Strategy | None = None) -> None:
        self._strategy: Strategy = strategy or Counter()
        self._long_to_short: dict[str, str] = {}
        self._short_to_long: dict[str, str] = {}
        self._lock = threading.Lock()

    def shorten(self, long_url: str) -> str:
        """Return the short URL for `long_url`, generating one if needed.

        Idempotent — repeated calls with the same `long_url` return the same short.
        Raises CollisionError if the strategy returns a short already bound to a
        different long_url.
        """
        with self._lock:
            if existing := self._long_to_short.get(long_url):
                return existing

            short = self._strategy(long_url)
            collision = self._short_to_long.get(short)
            if collision is not None and collision != long_url:
                raise CollisionError(f"short {short!r} already maps to {collision!r}")

            self._long_to_short[long_url] = short
            self._short_to_long[short] = long_url
            return short

    def expand(self, short_url: str) -> str:
        """Return the long URL for `short_url`. Raises UnknownShortURLError if not found."""
        with self._lock:
            try:
                return self._short_to_long[short_url]
            except KeyError:
                raise UnknownShortURLError(short_url) from None

    def __len__(self) -> int:
        with self._lock:
            return len(self._long_to_short)

    def __contains__(self, long_url: object) -> bool:
        with self._lock:
            return long_url in self._long_to_short
