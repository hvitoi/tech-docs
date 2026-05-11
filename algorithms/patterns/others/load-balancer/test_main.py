import unittest
from concurrent.futures import ThreadPoolExecutor

from main import (
    LoadBalancer,
    NoServersAvailableError,
    PoolFullError,
    RoundRobin,
    random_choice,
)


class TestRegisterAndCapacity(unittest.TestCase):
    def test_register_adds_server(self):
        lb = LoadBalancer()
        lb.register("a")
        lb.register("b")
        lb.register("c")
        self.assertEqual(len(lb), 3)

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

    def test_invalid_capacity_raises(self):
        with self.assertRaises(ValueError):
            LoadBalancer(max_targets=0)
        with self.assertRaises(ValueError):
            LoadBalancer(max_targets=-1)


class TestUnregister(unittest.TestCase):
    def test_unregister_frees_slot(self):
        lb = LoadBalancer()
        lb.register("a")
        lb.register("b")
        lb.unregister("b")
        self.assertEqual(len(lb), 1)


class TestPick(unittest.TestCase):
    def test_pick(self):
        lb = LoadBalancer()
        lb.register("a")
        self.assertEqual(lb.pick(), "a")

    def test_pick_raises_on_empty_pool(self):
        lb = LoadBalancer()
        with self.assertRaises(NoServersAvailableError):
            lb.pick()


class TestStrategies(unittest.TestCase):
    def test_round_robin_cycles_through_servers(self):
        lb = LoadBalancer(strategy=RoundRobin())
        for s in "abc":
            lb.register(s)
        picked = [lb.pick() for _ in range(7)]
        self.assertEqual(picked, ["a", "b", "c", "a", "b", "c", "a"])

    def test_random_choice_covers_all_members(self):
        lb = LoadBalancer(strategy=random_choice)
        for s in "abc":
            lb.register(s)
        picked = {lb.pick() for _ in range(200)}
        self.assertEqual(picked, {"a", "b", "c"})


class TestConcurrency(unittest.TestCase):
    def test_concurrent_register_respects_capacity(self):
        """Threads racing must never overflow the server maximum capacity."""
        lb = LoadBalancer(max_targets=10)

        def register_many(thread_name: str) -> None:
            for i in range(20):
                try:
                    lb.register(f"{thread_name}-{i}")
                except PoolFullError:
                    return

        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(register_many, ["Thread-A", "Thread-B", "Thread-C"])

        self.assertEqual(len(lb), 10)

    def test_pick_under_concurrent_register(self):
        """pick() must keep working while another thread is registering."""
        lb = LoadBalancer(max_targets=1000)
        lb.register("a")

        def keep_registering() -> None:
            for i in range(999):
                lb.register(f"r-{i}")

        def keep_getting() -> None:
            for _ in range(1000):
                self.assertTrue(lb.pick())

        with ThreadPoolExecutor(max_workers=2) as executor:
            f1 = executor.submit(keep_registering)
            f2 = executor.submit(keep_getting)
            f1.result()
            f2.result()


if __name__ == "__main__":
    unittest.main()
