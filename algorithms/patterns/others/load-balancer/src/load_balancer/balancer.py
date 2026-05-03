import threading

from load_balancer.strategies import RoundRobin, Strategy


class NoServersAvailableError(RuntimeError):
    """Raised when `get()` is called on an empty pool."""


class LoadBalancer:
    def __init__(
        self,
        max_servers: int = 10,
        strategy: Strategy | None = None,
    ) -> None:
        if max_servers <= 0:
            raise ValueError("max_servers must be positive")
        self._max_servers = max_servers
        self._servers: list[str] = []
        self._lock = threading.Lock()
        self._strategy: Strategy = strategy or RoundRobin()

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
            raise NoServersAvailableError
        return self._strategy(snapshot)

    def __len__(self) -> int:
        with self._lock:
            return len(self._servers)

    def __contains__(self, server: object) -> bool:
        with self._lock:
            return server in self._servers
