"""
A strategy is any callable that picks one server from a non-empty pool:
  - Stateless strategies: plain functions;
  - Stateful strategies: callable classes (e.g., round-robin)
  - Custom strategies need only match the `Strategy` type.
"""

import random
import threading
from collections.abc import Callable, Sequence

type Strategy = Callable[[Sequence[str]], str]


def random_choice(servers: Sequence[str]) -> str:
    """Uniform random pick."""
    return random.choice(servers)


class RoundRobin:
    """
    Select a different server each time in the order that they appear in the sequence
    The lock protects the "_index" resource. It guarantees no lost updates / interleaved accesses

    Example:
        - Thread A: reads _index → gets 5
        - Thread B: reads _index → gets 5      ← both read the same value
        - Thread A: computes i=5, writes _index = 6
        - Thread B: computes i=5, writes _index = 6  ← second write clobbers, but both threads also returned servers[5]
    """

    def __init__(self) -> None:
        self._index = 0
        self._lock = threading.Lock()

    def __call__(self, servers: Sequence[str]) -> str:
        with self._lock:  # pessimistic lock
            # mod handles pool shrinking between calls (if the pool shrinks between calls, it won't get an index out of range error)
            i = self._index % len(servers)
            self._index = i + 1
            return servers[i]
