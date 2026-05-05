import pytest
from load_balancer.balancer import (
    LoadBalancer,
    NoServersAvailableError,
    RoundRobin,
)
from load_balancer.strategies import random_choice


def test_round_robin_cycles_and_handles_shrinkage():
    rr = RoundRobin()
    servers = ["a", "b", "c"]
    assert [rr(servers) for _ in range(5)] == ["a", "b", "c", "a", "b"]

    # modulo keeps the index valid when the pool shrinks below it
    servers.pop()
    assert rr(servers) in {"a", "b"}


def test_default_strategy_is_round_robin():
    lb = LoadBalancer()
    for s in "abc":
        lb.register(s)
    assert [lb.get() for _ in range(4)] == ["a", "b", "c", "a"]


def test_random_choice_covers_all_members():
    servers = ["a", "b", "c"]
    seen = {random_choice(servers) for _ in range(200)}
    assert seen == set(servers)


def test_balancer_accepts_arbitrary_callable_strategy():
    lb = LoadBalancer(strategy=lambda servers: servers[0])
    lb.register("a")
    lb.register("b")
    assert lb.get() == "a"
    assert lb.get() == "a"


def test_empty_pool_raises_through_balancer():
    lb = LoadBalancer()
    with pytest.raises(NoServersAvailableError):
        lb.get()
