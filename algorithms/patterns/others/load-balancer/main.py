import random
import threading
from collections.abc import Callable

# --- strategies ---


type Strategy = Callable[[list[str]], str]


def random_choice(servers: list[str]) -> str:
    """Stateless strategy"""
    return random.choice(servers)


class RoundRobin:
    """Stateful strategy"""

    def __init__(self) -> None:
        self.counter = 0
        self._lock = threading.Lock()

    def __call__(self, servers: list[str]) -> str:
        with self._lock:
            i = self.counter % len(servers)
            self.counter += 1  # A billion calls it's a 30-bit int (4 bytes). You will not exhaust memory.
            return servers[i]


# --- balancer ---


class NoServersAvailableError(RuntimeError): ...


class PoolFullError(RuntimeError): ...


class LoadBalancer:
    def __init__(
        self,
        max_servers: int = 10,
        strategy: Strategy | None = None,
    ) -> None:
        if max_servers <= 0:
            raise ValueError("Capacity must be positive")
        self.max_servers = max_servers
        self.strategy: Strategy = strategy or RoundRobin()
        self.servers: list[str] = []
        self._lock = threading.Lock()

    def register(self, server: str) -> None:
        with self._lock:
            if server in self.servers:
                return  # idempotent
            if len(self.servers) >= self.max_servers:
                raise PoolFullError(f"pool is full ({self.max_servers} servers)")
            self.servers.append(server)

    def unregister(self, server: str) -> None:
        with self._lock:
            self.servers.remove(server)

    def pick(self) -> str:
        with self._lock:
            # copy under lock (take a copy and release the lock)
            snapshot = list(self.servers)
        if not snapshot:
            raise NoServersAvailableError

        # with the snapshot, I can do the slow work outside
        # Specially considering that the callable is user-defined and you have no control over it
        # It also protects the strategy from a concurrent mutation (e.g., iterating over a list with mutating indexes)
        # a strategy is immutable from the strategy's point of view
        # It also decouples the strategy from the balancer's concurrency model (two independent locks)
        return self.strategy(snapshot)  # run outside lock

    def __len__(self) -> int:
        with self._lock:
            return len(self.servers)

    def __contains__(self, server: object) -> bool:
        with self._lock:
            return server in self.servers
