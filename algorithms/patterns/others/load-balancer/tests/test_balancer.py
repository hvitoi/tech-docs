"""Tests for `LoadBalancer` register / unregister / get / dunder methods."""

import pytest

from load_balancer import LoadBalancer, NoServersAvailableError


# --- register ---


def test_register_returns_true_for_new_server():
    lb = LoadBalancer()
    assert lb.register("a") is True


def test_register_returns_false_for_duplicate():
    lb = LoadBalancer()
    lb.register("a")
    assert lb.register("a") is False


def test_register_returns_false_when_full():
    lb = LoadBalancer(max_servers=2)
    lb.register("a")
    lb.register("b")
    assert lb.register("c") is False


def test_register_raises_for_zero_capacity():
    with pytest.raises(ValueError):
        LoadBalancer(max_servers=0)


def test_register_raises_for_negative_capacity():
    with pytest.raises(ValueError):
        LoadBalancer(max_servers=-1)


# --- unregister ---


def test_unregister_returns_true_when_present():
    lb = LoadBalancer()
    lb.register("a")
    assert lb.unregister("a") is True
    assert "a" not in lb


def test_unregister_returns_false_when_absent():
    lb = LoadBalancer()
    assert lb.unregister("a") is False


def test_register_after_unregister_succeeds():
    lb = LoadBalancer(max_servers=1)
    lb.register("a")
    lb.unregister("a")
    assert lb.register("a") is True


# --- get ---


def test_get_raises_on_empty_pool():
    lb = LoadBalancer()
    with pytest.raises(NoServersAvailableError):
        lb.get()


def test_get_after_all_unregistered_raises():
    lb = LoadBalancer()
    lb.register("a")
    lb.unregister("a")
    with pytest.raises(NoServersAvailableError):
        lb.get()


# --- dunder methods ---


def test_len_reflects_pool_size():
    lb = LoadBalancer()
    assert len(lb) == 0
    lb.register("a")
    lb.register("b")
    assert len(lb) == 2


def test_contains():
    lb = LoadBalancer()
    lb.register("a")
    assert "a" in lb
    assert "b" not in lb
