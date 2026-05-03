"""Smoke tests for thread safety.

These tests don't *prove* the absence of races (you can't, in finite time),
but they exercise enough concurrency to surface common bugs.
"""

import threading

from load_balancer import LoadBalancer


def test_register_is_thread_safe_no_duplicates():
    lb = LoadBalancer(max_servers=100)

    def worker(prefix: str) -> None:
        for i in range(50):
            lb.register(f"{prefix}-{i}")

    threads = [threading.Thread(target=worker, args=(p,)) for p in ("x", "y")]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(lb) == 100  # 50 + 50, no double-register


def test_register_capacity_respected_under_concurrency():
    """Many threads racing to register past capacity — pool size must not exceed max."""
    lb = LoadBalancer(max_servers=10)

    def worker(prefix: str) -> None:
        for i in range(20):
            lb.register(f"{prefix}-{i}")

    threads = [threading.Thread(target=worker, args=(p,)) for p in "abcde"]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(lb) == 10


def test_get_under_concurrent_register_does_not_crash():
    """get() should never raise NoServersAvailableError once at least one server exists."""
    lb = LoadBalancer(max_servers=100)
    lb.register("seed")

    stop = threading.Event()

    def registerer() -> None:
        i = 0
        while not stop.is_set():
            lb.register(f"r-{i}")
            i += 1

    def getter() -> None:
        for _ in range(1000):
            assert lb.get()  # must always return a non-empty string

    reg_thread = threading.Thread(target=registerer)
    get_thread = threading.Thread(target=getter)

    reg_thread.start()
    get_thread.start()
    get_thread.join()
    stop.set()
    reg_thread.join()
