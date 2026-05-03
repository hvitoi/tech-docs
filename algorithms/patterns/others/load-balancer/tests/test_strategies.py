"""Tests for selection strategies."""

import pytest

from load_balancer import LoadBalancer, RandomStrategy, RoundRobinStrategy


# --- round-robin ---


def test_round_robin_cycles_through_servers():
    rr = RoundRobinStrategy()
    servers = ["a", "b", "c"]
    assert [rr.select(servers) for _ in range(7)] == ["a", "b", "c", "a", "b", "c", "a"]


def test_round_robin_handles_pool_shrinkage():
    """If the pool shrinks between selects, the modulo keeps the index valid."""
    rr = RoundRobinStrategy()
    rr.select(["a", "b", "c"])
    rr.select(["a", "b", "c"])
    rr.select(["a", "b", "c"])
    # pool now smaller — must still pick a valid member
    assert rr.select(["a", "b"]) in {"a", "b"}


def test_load_balancer_default_strategy_is_round_robin():
    lb = LoadBalancer()
    for s in ["a", "b", "c"]:
        lb.register(s)
    assert [lb.get() for _ in range(7)] == ["a", "b", "c", "a", "b", "c", "a"]


# --- random ---


def test_random_returns_member_of_pool():
    r = RandomStrategy()
    assert r.select(["a", "b", "c"]) in {"a", "b", "c"}


def test_random_distribution_covers_all_servers():
    r = RandomStrategy()
    seen = {r.select(["a", "b", "c"]) for _ in range(200)}
    # not strictly guaranteed but vanishingly unlikely to fail
    assert seen == {"a", "b", "c"}


# --- strategy injection ---


def test_load_balancer_uses_injected_strategy():
    lb = LoadBalancer(strategy=RandomStrategy())
    for s in ["a", "b", "c"]:
        lb.register(s)
    assert lb.get() in {"a", "b", "c"}


# --- empty pool propagation ---


@pytest.mark.parametrize("strategy", [RoundRobinStrategy, RandomStrategy])
def test_strategy_handles_empty_pool_via_balancer(strategy):
    """Empty-pool handling is the LoadBalancer's job, not the strategy's —
    but the LoadBalancer must catch it before calling strategy.select."""
    from load_balancer import NoServersAvailableError

    lb = LoadBalancer(strategy=strategy())
    with pytest.raises(NoServersAvailableError):
        lb.get()
