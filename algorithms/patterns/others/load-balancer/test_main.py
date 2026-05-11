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

    def test_register_idempotent_on_full_pool(self):
        """Re-registering an existing server in a full pool must not raise."""
        lb = LoadBalancer(max_targets=2)
        lb.register("a")
        lb.register("b")
        lb.register("a")
        self.assertEqual(len(lb), 2)

    def test_invalid_capacity_raises(self):
        for n in (0, -1):
            with self.subTest(n=n), self.assertRaises(ValueError):
                LoadBalancer(max_targets=n)


class TestUnregister(unittest.TestCase):
    def test_unregister_frees_slot(self):
        lb = LoadBalancer(max_targets=1)
        lb.register("a")
        lb.unregister("a")
        self.assertNotIn("a", lb)
        lb.register("a")  # slot freed


class TestGet(unittest.TestCase):
    def test_get_raises_on_empty_pool(self):
        lb = LoadBalancer()
        with self.assertRaises(NoServersAvailableError):
            lb.pick()


class TestDunders(unittest.TestCase):
    def test_len_and_contains(self):
        lb = LoadBalancer()
        self.assertEqual(len(lb), 0)
        self.assertNotIn("a", lb)
        lb.register("a")
        self.assertEqual(len(lb), 1)
        self.assertIn("a", lb)


class TestStrategies(unittest.TestCase):
    def test_round_robin_cycles_through_servers(self):
        lb = LoadBalancer()
        for s in "abc":
            lb.register(s)
        self.assertEqual(
            [lb.pick() for _ in range(7)],
            ["a", "b", "c", "a", "b", "c", "a"],
        )

    def test_round_robin_handles_pool_shrinkage(self):
        rr = RoundRobin()
        for _ in range(3):
            rr(["a", "b", "c"])
        self.assertIn(rr(["a", "b"]), {"a", "b"})

    def test_balancer_accepts_arbitrary_callable_strategy(self):
        lb = LoadBalancer(strategy=lambda servers: servers[0])
        lb.register("a")
        lb.register("b")
        self.assertEqual(lb.pick(), "a")
        self.assertEqual(lb.pick(), "a")

    def test_random_choice_covers_all_members(self):
        seen = {random_choice(["a", "b", "c"]) for _ in range(200)}
        self.assertEqual(seen, {"a", "b", "c"})


class TestConcurrency(unittest.TestCase):
    def test_concurrent_register_respects_capacity(self):
        """Threads racing must never overflow the server maximum capacity."""
        lb = LoadBalancer(max_targets=10)

        def register_many(prefix: str) -> None:
            for i in range(20):
                try:
                    lb.register(f"{prefix}-{i}")
                except PoolFullError:
                    return

        with ThreadPoolExecutor(max_workers=3) as ex:
            list(ex.map(register_many, "abc"))
        self.assertEqual(len(lb), 10)

    def test_get_under_concurrent_register(self):
        """get() must keep working while another thread is registering."""
        lb = LoadBalancer(max_targets=1000)
        lb.register("seed")

        def keep_registering() -> None:
            for i in range(999):
                lb.register(f"r-{i}")

        def keep_getting() -> None:
            for _ in range(1000):
                self.assertTrue(lb.pick())

        with ThreadPoolExecutor(max_workers=2) as ex:
            f1 = ex.submit(keep_registering)
            f2 = ex.submit(keep_getting)
            f1.result()
            f2.result()


if __name__ == "__main__":
    unittest.main()
