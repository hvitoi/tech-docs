import pytest

from load_balancer.balancer import LoadBalancer, NoServersAvailableError, PoolFullError


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


@pytest.mark.parametrize("n", [0, -1])
def test_invalid_capacity_raises(n):
    with pytest.raises(ValueError):
        LoadBalancer(max_servers=n)


def test_unregister_removes_server():
    lb = LoadBalancer(max_servers=1)
    lb.register("a")
    lb.unregister("a")
    assert "a" not in lb
    lb.register("a")  # slot freed


def test_get_raises_on_empty_pool():
    lb = LoadBalancer()
    with pytest.raises(NoServersAvailableError):
        lb.get()


def test_len_and_contains():
    lb = LoadBalancer()
    assert len(lb) == 0 and "a" not in lb
    lb.register("a")
    assert len(lb) == 1 and "a" in lb
