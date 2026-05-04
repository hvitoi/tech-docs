"""Smoke tests for thread safety. They cannot prove the absence of races,
but they exercise enough concurrency to surface common bugs."""

import threading

from load_balancer import LoadBalancer, PoolFullError


def test_concurrent_register_respects_capacity():
    """Threads racing past capacity must never overflow the pool."""
    lb = LoadBalancer(max_servers=10)

    def worker(prefix: str) -> None:
        for i in range(20):
            try:
                lb.register(f"{prefix}-{i}")
            except PoolFullError:
                return

    threads = [threading.Thread(target=worker, args=(p,)) for p in "abcde"]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(lb) == 10


def test_get_under_concurrent_register():
    """get() must always succeed while another thread is registering."""
    lb = LoadBalancer(max_servers=1000)
    lb.register("seed")
    stop = threading.Event()

    def registerer() -> None:
        i = 0
        while not stop.is_set():
            try:
                lb.register(f"r-{i}")
            except PoolFullError:
                return
            i += 1

    def getter() -> None:
        for _ in range(1000):
            assert lb.get()

    reg = threading.Thread(target=registerer)
    get = threading.Thread(target=getter)
    reg.start()
    get.start()
    get.join()
    stop.set()
    reg.join()
