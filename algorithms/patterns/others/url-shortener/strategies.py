"""
A strategy is any callable that produces a short identifier for a long URL:
  - Stateless strategies: plain functions (deterministic, hash-based)
  - Stateful strategies: callable classes (e.g., counter)
  - Custom strategies need only match the `Strategy` type.
"""

import base64
import hashlib
import itertools
import random
import string
import threading
from collections.abc import Callable

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
    """
    Monotonic incrementing identifier — ignores long_url, just hands out the next int.

    The lock protects the underlying counter from lost updates / interleaved access.
    """

    def __init__(self) -> None:
        self._counter = itertools.count(1)
        self._lock = threading.Lock()

    def __call__(self, _long_url: str) -> str:
        with self._lock:
            return str(next(self._counter))
