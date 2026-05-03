from __future__ import annotations

import threading

from load_balancer.errors import NoServersAvailableError
from load_balancer.strategies import RoundRobinStrategy, SelectionStrategy


class LoadBalancer:
    """Distributes requests across a pool of registered servers.

    Operations:
    - `register(server)` — add to the pool. Returns False on duplicate or full pool.
    - `unregister(server)` — remove from the pool. Returns False if not present.
    - `get()` — select a server via the configured strategy. Raises on empty.

    Thread-safe: a single lock guards all pool mutations and reads. The
    strategy's `select` is called with a snapshot — the lock is released
    before `select` runs to avoid contention.
    """

    def __init__(
        self,
        max_servers: int = 10,
        strategy: SelectionStrategy | None = None,
    ) -> None:
        if max_servers <= 0:
            raise ValueError("max_servers must be positive")
        self._max_servers = max_servers
        self._servers: list[str] = []
        self._lock = threading.Lock()
        self._strategy = strategy if strategy is not None else RoundRobinStrategy()

    def register(self, server: str) -> bool:
        with self._lock:
            if len(self._servers) >= self._max_servers or server in self._servers:
                return False
            self._servers.append(server)
            return True

    def unregister(self, server: str) -> bool:
        with self._lock:
            try:
                self._servers.remove(server)
                return True
            except ValueError:
                return False

    def get(self) -> str:
        with self._lock:
            snapshot = list(self._servers)  # snapshot, then release the lock
        if not snapshot:
            raise NoServersAvailableError()
        return self._strategy.select(snapshot)

    # Pythonic protocols
    def __len__(self) -> int:
        with self._lock:
            return len(self._servers)

    def __contains__(self, server: str) -> bool:
        with self._lock:
            return server in self._servers
