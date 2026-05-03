"""Selection strategies for `LoadBalancer`.

A strategy is any callable that picks one server from a non-empty pool.
Stateless strategies are plain functions; stateful ones (round-robin) are
callable classes. Custom strategies need only match the `Strategy` type.
"""

import random
import threading
from collections.abc import Callable, Sequence

type Strategy = Callable[[Sequence[str]], str]


def random_choice(servers: Sequence[str]) -> str:
    """Uniform random pick."""
    return random.choice(servers)


class RoundRobin:
    """Cycle through servers in registration order. Thread-safe."""

    def __init__(self) -> None:
        self._index = 0
        self._lock = threading.Lock()

    def __call__(self, servers: Sequence[str]) -> str:
        with self._lock:
            i = self._index % len(servers)  # mod handles pool shrinking between calls
            self._index = i + 1
            return servers[i]
