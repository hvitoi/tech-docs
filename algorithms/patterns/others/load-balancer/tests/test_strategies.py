"""Tests for selection strategies."""

import pytest

from load_balancer import (
    LoadBalancer,
    NoServersAvailableError,
    RoundRobin,
    Strategy,
    random_choice,
)


# --- round-robin ---


def test_round_robin_cycles_through_servers():
    rr = RoundRobin()
    servers = ["a", "b", "c"]
    assert [rr(servers) for _ in range(7)] == ["a", "b", "c", "a", "b", "c", "a"]


def test_round_robin_handles_pool_shrinkage():
    """If the pool shrinks between selects, the modulo keeps the index valid."""
    rr = RoundRobin()
    rr(["a", "b", "c"])
    rr(["a", "b", "c"])
    rr(["a", "b", "c"])
    assert rr(["a", "b"]) in {"a", "b"}


def test_load_balancer_default_strategy_is_round_robin():
    lb = LoadBalancer()
    for s in ["a", "b", "c"]:
        lb.register(s)
    assert [lb.get() for _ in range(7)] == ["a", "b", "c", "a", "b", "c", "a"]


# --- random ---


def test_random_choice_returns_member_of_pool():
    assert random_choice(["a", "b", "c"]) in {"a", "b", "c"}


def test_random_choice_distribution_covers_all_servers():
    seen = {random_choice(["a", "b", "c"]) for _ in range(200)}
    assert seen == {"a", "b", "c"}


# --- strategy injection (any callable works) ---


def test_balancer_accepts_function_strategy():
    lb = LoadBalancer(strategy=random_choice)
    for s in ["a", "b", "c"]:
        lb.register(s)
    assert lb.get() in {"a", "b", "c"}


def test_balancer_accepts_class_strategy():
    lb = LoadBalancer(strategy=RoundRobin())
    for s in ["a", "b", "c"]:
        lb.register(s)
    assert lb.get() == "a"


def test_balancer_accepts_lambda_strategy():
    """A `Strategy` is just a callable — anything matching the signature works."""
    always_first: Strategy = lambda servers: servers[0]
    lb = LoadBalancer(strategy=always_first)
    lb.register("a")
    lb.register("b")
    assert lb.get() == "a"


# --- empty pool propagation ---


@pytest.mark.parametrize("strategy_factory", [RoundRobin, lambda: random_choice])
def test_empty_pool_raises_via_balancer(strategy_factory):
    lb = LoadBalancer(strategy=strategy_factory())
    with pytest.raises(NoServersAvailableError):
        lb.get()
