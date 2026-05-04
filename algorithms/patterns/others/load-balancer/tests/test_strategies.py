import pytest

from load_balancer import (
    LoadBalancer,
    NoServersAvailableError,
    RoundRobin,
    Strategy,
    random_choice,
)


def test_round_robin_cycles_and_handles_shrinkage():
    rr = RoundRobin()
    assert [rr(["a", "b", "c"]) for _ in range(4)] == ["a", "b", "c", "a"]
    # modulo keeps the index valid when the pool shrinks below it
    assert rr(["a", "b"]) in {"a", "b"}


def test_default_strategy_is_round_robin():
    lb = LoadBalancer()
    for s in "abc":
        lb.register(s)
    assert [lb.get() for _ in range(4)] == ["a", "b", "c", "a"]


def test_random_choice_covers_all_members():
    seen = {random_choice(["a", "b", "c"]) for _ in range(200)}
    assert seen == {"a", "b", "c"}


def test_balancer_accepts_arbitrary_callable_strategy():
    always_first: Strategy = lambda servers: servers[0]
    lb = LoadBalancer(strategy=always_first)
    lb.register("a")
    lb.register("b")
    assert lb.get() == "a"


@pytest.mark.parametrize("strategy", [RoundRobin(), random_choice])
def test_empty_pool_raises_through_balancer(strategy):
    lb = LoadBalancer(strategy=strategy)
    with pytest.raises(NoServersAvailableError):
        lb.get()
