import random
import threading
from collections.abc import Callable, Sequence

# --- strategies ---


type Strategy = Callable[[Sequence[str]], str]


def random_choice(servers: Sequence[str]) -> str:
    """Stateless strategy"""
    return random.choice(servers)


class RoundRobin:
    """Stateful strategy"""

    def __init__(self) -> None:
        self._counter = 0
        self._lock = threading.Lock()

    def __call__(self, servers: Sequence[str]) -> str:
        with self._lock:
            i = self._counter % len(servers)
            self._counter += 1  # A billion calls it's a 30-bit int (4 bytes). You will not exhaust memory.
            return servers[i]


# --- balancer ---


class NoServersAvailableError(RuntimeError): ...


class PoolFullError(RuntimeError): ...


class LoadBalancer:
    def __init__(
        self,
        max_targets: int = 10,
        strategy: Strategy | None = None,
    ) -> None:
        if max_targets <= 0:
            raise ValueError("max_servers must be positive")
        self._max_targets = max_targets
        self._strategy: Strategy = strategy or RoundRobin()
        self._targets: list[str] = []
        self._lock = threading.Lock()

    def register(self, server: str) -> None:
        with self._lock:
            if server in self._targets:
                return  # idempotent
            if len(self._targets) >= self._max_targets:
                raise PoolFullError(f"pool is full ({self._max_targets} servers)")
            self._targets.append(server)

    def unregister(self, server: str) -> None:
        with self._lock:
            self._targets.remove(server)

    def pick(self) -> str:
        with self._lock:
            # copy under lock (take a copy and release the lock)
            snapshot = list(self._targets)
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
            return len(self._targets)

    def __contains__(self, target: object) -> bool:
        with self._lock:
            return target in self._targets
