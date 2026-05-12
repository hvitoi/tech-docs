import unittest
from concurrent.futures import ThreadPoolExecutor

from main import LoadBalancer, NoServersAvailableError, PoolFullError, RoundRobin


class TestLoadBalancer(unittest.TestCase):
    def test_register_adds_server(self):
        lb = LoadBalancer()
        lb.register("a")
        lb.register("b")
        self.assertEqual(len(lb), 2)

    def test_register_is_idempotent(self):
        lb = LoadBalancer()
        lb.register("a")
        lb.register("a")
        self.assertEqual(len(lb), 1)

    def test_register_raises_when_full(self):
        lb = LoadBalancer(max_targets=1)
        lb.register("a")
        with self.assertRaises(PoolFullError):
            lb.register("b")

    def test_unregister_frees_slot(self):
        lb = LoadBalancer()
        lb.register("a")
        lb.unregister("a")
        self.assertEqual(len(lb), 0)

    def test_pick_raises_on_empty_pool(self):
        lb = LoadBalancer()
        with self.assertRaises(NoServersAvailableError):
            lb.pick()

    def test_round_robin_cycles_through_servers(self):
        lb = LoadBalancer(strategy=RoundRobin())
        for s in "abc":
            lb.register(s)
        picked = [lb.pick() for _ in range(7)]
        self.assertEqual(picked, ["a", "b", "c", "a", "b", "c", "a"])

    def test_concurrent_register_respects_capacity(self):
        lb = LoadBalancer(max_targets=10)
        with ThreadPoolExecutor(max_workers=3) as ex:
            ex.map(lambda i: _try_register(lb, i), range(50))
        self.assertEqual(len(lb), 10)


def _try_register(lb: LoadBalancer, i: int) -> None:
    try:
        lb.register(f"s-{i}")
    except PoolFullError:
        pass


if __name__ == "__main__":
    unittest.main()
