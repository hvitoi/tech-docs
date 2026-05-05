import random
import threading
from collections.abc import Callable, Sequence

# --- strategies ---


type Strategy = Callable[[Sequence[str]], str]


def random_choice(servers: Sequence[str]) -> str:
    """Uniform random pick. Stateless."""
    return random.choice(servers)


class RoundRobin:
    """Cycle through servers in order. Thread-safe via internal lock.

    The lock guards the read-modify-write of _counter against lost updates
    when multiple threads call __call__ concurrently.
    """

    def __init__(self) -> None:
        self._counter = 0
        self._lock = threading.Lock()

    def __call__(self, servers: Sequence[str]) -> str:
        with self._lock:
            i = self._counter % len(servers)
            self._counter += 1  # A billion calls it's a 30-bit int (4 bytes). You will not exhaust memory.
            return servers[i]


# --- errors + balancer ---


class NoServersAvailableError(RuntimeError):
    """Raised when get() is called on an empty pool."""


class PoolFullError(RuntimeError):
    """Raised when register() is called on a full pool."""


class LoadBalancer:
    """Distributes requests across a pool of registered servers.

    `register` is idempotent (re-registering an existing server is a no-op).
    `get` snapshots the pool under the lock, then runs the strategy outside
    the lock so a slow/buggy strategy can't block other operations.
    """

    def __init__(
        self,
        max_servers: int = 10,
        strategy: Strategy | None = None,
    ) -> None:
        if max_servers <= 0:
            raise ValueError("max_servers must be positive")
        self._max_servers = max_servers
        self._strategy: Strategy = strategy or RoundRobin()
        self._servers: list[str] = []
        self._lock = threading.Lock()

    def register(self, server: str) -> None:
        with self._lock:
            if server in self._servers:
                return  # idempotent
            if len(self._servers) >= self._max_servers:
                raise PoolFullError(f"pool is full ({self._max_servers} servers)")
            self._servers.append(server)

    def unregister(self, server: str) -> None:
        with self._lock:
            self._servers.remove(server)

    def get(self) -> str:
        with self._lock:
            # copy under lock (take a copy and release the lock)
            snapshot = list(self._servers)
        if not snapshot:
            raise NoServersAvailableError

        # with the snapshot, I can do the slow work outside
        # Specially considering that the callable is user-defined and you have no control over it
        # It also protects the strategy from a concurrent mutation (e.g., iterating over a list with mutating indexes)
        # a strategy is immutable from the strategy's point of view
        # It also decouples the strategy from the balancer's concurrency model (two independent locks)
        return self._strategy(snapshot)  # run outside lock

    def __len__(self) -> int:
        with self._lock:
            return len(self._servers)

    def __contains__(self, server: object) -> bool:
        with self._lock:
            return server in self._servers
