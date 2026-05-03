"""Selection strategies — pick one server from a pool snapshot.

Each strategy is responsible only for picking; the pool is owned by the
`LoadBalancer`. Strategies receive a snapshot, so they're free of pool-mutation
concerns.
"""

from __future__ import annotations

import random
import threading
from abc import ABC, abstractmethod
from typing import Sequence


class SelectionStrategy(ABC):
    """Picks one server from a non-empty pool snapshot."""

    @abstractmethod
    def select(self, servers: Sequence[str]) -> str: ...


class RoundRobinStrategy(SelectionStrategy):
    """Cycle through servers in registration order.

    The internal index is guarded by its own lock — the load balancer's pool
    lock doesn't need to be held during selection.
    """

    def __init__(self) -> None:
        self._index = 0
        self._lock = threading.Lock()

    def select(self, servers: Sequence[str]) -> str:
        with self._lock:
            i = self._index % len(servers)  # mod handles pool shrinking between calls
            self._index = i + 1
            return servers[i]


class RandomStrategy(SelectionStrategy):
    """Uniform random pick. Stateless, no lock needed."""

    def select(self, servers: Sequence[str]) -> str:
        return random.choice(servers)
