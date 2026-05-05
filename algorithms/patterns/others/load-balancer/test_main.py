from concurrent.futures import ThreadPoolExecutor

import pytest
from main import (
    LoadBalancer,
    NoServersAvailableError,
    PoolFullError,
    RoundRobin,
    random_choice,
)

# --- register / capacity ---


def test_register_is_idempotent():
    lb = LoadBalancer()
    lb.register("a")
    lb.register("a")
    assert len(lb) == 1


def test_register_raises_when_full():
    lb = LoadBalancer(max_servers=1)
    lb.register("a")
    with pytest.raises(PoolFullError):
        lb.register("b")


def test_register_idempotent_on_full_pool():
    """Re-registering an existing server in a full pool must not raise."""
    lb = LoadBalancer(max_servers=2)
    lb.register("a")
    lb.register("b")
    lb.register("a")  # no exception
    assert len(lb) == 2


@pytest.mark.parametrize("n", [0, -1])
def test_invalid_capacity_raises(n):
    with pytest.raises(ValueError):
        LoadBalancer(max_servers=n)


# --- unregister ---


def test_unregister_frees_slot():
    lb = LoadBalancer(max_servers=1)
    lb.register("a")
    lb.unregister("a")
    assert "a" not in lb
    lb.register("a")  # slot freed


# --- get / empty pool ---


def test_get_raises_on_empty_pool():
    lb = LoadBalancer()
    with pytest.raises(NoServersAvailableError):
        lb.get()


# --- dunder methods ---


def test_len_and_contains():
    lb = LoadBalancer()
    assert len(lb) == 0 and "a" not in lb
    lb.register("a")
    assert len(lb) == 1 and "a" in lb


# --- strategies ---


def test_round_robin_cycles_through_servers():
    lb = LoadBalancer()
    for s in "abc":
        lb.register(s)
    assert [lb.get() for _ in range(7)] == ["a", "b", "c", "a", "b", "c", "a"]


def test_round_robin_handles_pool_shrinkage():
    rr = RoundRobin()
    for _ in range(3):
        rr(["a", "b", "c"])
    assert rr(["a", "b"]) in {"a", "b"}


def test_balancer_accepts_arbitrary_callable_strategy():
    lb = LoadBalancer(strategy=lambda servers: servers[0])
    lb.register("a")
    lb.register("b")
    assert lb.get() == "a"
    assert lb.get() == "a"


def test_random_choice_covers_all_members():
    seen = {random_choice(["a", "b", "c"]) for _ in range(200)}
    assert seen == {"a", "b", "c"}


# --- concurrency ---


def test_concurrent_register_respects_capacity():
    """Threads racing must never overflow the server maximum capacity."""
    lb = LoadBalancer(max_servers=10)

    def register_many(prefix: str) -> None:
        for i in range(20):
            try:
                lb.register(f"{prefix}-{i}")
            except PoolFullError:
                return

    with ThreadPoolExecutor(max_workers=3) as ex:
        list(ex.map(register_many, "abc"))
    assert len(lb) == 10


def test_get_under_concurrent_register():
    """get() must keep working while another thread is registering."""
    lb = LoadBalancer(max_servers=1000)
    lb.register("seed")

    def keep_registering() -> None:
        for i in range(999):
            lb.register(f"r-{i}")

    def keep_getting() -> None:
        for _ in range(1000):
            assert lb.get()

    with ThreadPoolExecutor(max_workers=2) as ex:
        f1 = ex.submit(keep_registering)
        f2 = ex.submit(keep_getting)
        f1.result()
        f2.result()
