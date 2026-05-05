from concurrent.futures import ThreadPoolExecutor

from load_balancer.balancer import LoadBalancer, PoolFullError


def test_concurrent_register_respects_capacity():
    """Threads racing must never overflow the server maximum capacity"""
    lb = LoadBalancer(max_servers=10)

    def register_20_servers(thread_name: str) -> None:
        for i in range(20):
            try:
                lb.register(f"{thread_name}-{i}")
            except PoolFullError:
                return

    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(register_20_servers, "abc")

    assert len(lb) == 10


def test_get_under_concurrent_register():
    """get() must always succeed while another thread is registering."""
    lb = LoadBalancer(max_servers=1000)
    lb.register("myserver.com")

    def registerer() -> None:
        for i in range(999):
            lb.register(f"r-{i}")

    def getter() -> None:
        for _ in range(1000):
            assert lb.get()

    with ThreadPoolExecutor(max_workers=2) as executor:
        f1 = executor.submit(registerer)  # keep registering in background
        f2 = executor.submit(getter)  # keep getting in background (while registering)
        f1.result()
        f2.result()  # re-raises if either thread raised
