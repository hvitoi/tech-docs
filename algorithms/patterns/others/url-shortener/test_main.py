import unittest
from concurrent.futures import ThreadPoolExecutor

from main import (
    CollisionError,
    Counter,
    UnknownShortURLError,
    URLShortener,
    base64_hash,
    md5_hash,
    random_string,
)


class TestShorten(unittest.TestCase):
    def test_shorten_is_idempotent(self):
        s = URLShortener(Counter())
        a = s.shorten("https://example.com")
        b = s.shorten("https://example.com")
        self.assertEqual(a, b)
        self.assertEqual(len(s), 1)

    def test_distinct_urls_get_distinct_shorts(self):
        s = URLShortener(Counter())
        a = s.shorten("https://example.com")
        b = s.shorten("https://other.com")
        self.assertNotEqual(a, b)
        self.assertEqual(len(s), 2)

    def test_collision_with_different_long_url_raises(self):
        """A strategy that returns a short already mapped to a different long URL must raise."""
        s = URLShortener(strategy=lambda _: "fixed-short")
        s.shorten("https://example.com")
        with self.assertRaises(CollisionError):
            s.shorten("https://other.com")


class TestExpand(unittest.TestCase):
    def test_expand_round_trip(self):
        s = URLShortener(Counter())
        short = s.shorten("https://example.com")
        self.assertEqual(s.expand(short), "https://example.com")

    def test_expand_unknown_raises(self):
        s = URLShortener(Counter())
        with self.assertRaises(UnknownShortURLError):
            s.expand("nope")


class TestDunders(unittest.TestCase):
    def test_default_strategy_is_counter(self):
        s = URLShortener()
        s.shorten("https://example.com")
        s.shorten("https://other.com")
        self.assertEqual(s.expand("1"), "https://example.com")
        self.assertEqual(s.expand("2"), "https://other.com")

    def test_len_and_contains(self):
        s = URLShortener()
        self.assertEqual(len(s), 0)
        self.assertNotIn("https://example.com", s)
        s.shorten("https://example.com")
        self.assertEqual(len(s), 1)
        self.assertIn("https://example.com", s)


class TestStrategies(unittest.TestCase):
    def test_counter_increments_per_call(self):
        c = Counter()
        self.assertEqual([c("any") for _ in range(3)], ["1", "2", "3"])

    def test_counter_ignores_long_url(self):
        c = Counter()
        a = c("https://example.com")
        b = c("https://other.com")
        self.assertEqual(int(b), int(a) + 1)

    def test_md5_is_deterministic(self):
        self.assertEqual(
            md5_hash("https://example.com"),
            md5_hash("https://example.com"),
        )

    def test_md5_distinct_inputs_distinct_shorts(self):
        self.assertNotEqual(md5_hash("https://a.com"), md5_hash("https://b.com"))

    def test_md5_short_length_is_8(self):
        self.assertEqual(len(md5_hash("https://example.com")), 8)

    def test_base64_is_deterministic(self):
        self.assertEqual(
            base64_hash("https://example.com"),
            base64_hash("https://example.com"),
        )

    def test_base64_short_length_is_8(self):
        self.assertEqual(len(base64_hash("https://example.com")), 8)

    def test_random_string_length_is_8(self):
        self.assertEqual(len(random_string("anything")), 8)

    def test_random_string_is_non_deterministic(self):
        """Two calls should differ — astronomically unlikely otherwise."""
        seen = {random_string("anything") for _ in range(100)}
        self.assertGreater(len(seen), 1)

    def test_shortener_accepts_arbitrary_callable_strategy(self):
        """A `Strategy` is just a callable — anything matching the signature works."""
        counter = iter("xyz")
        s = URLShortener(strategy=lambda _: next(counter))
        self.assertEqual(s.shorten("https://a.com"), "x")
        self.assertEqual(s.shorten("https://b.com"), "y")
        self.assertEqual(s.shorten("https://c.com"), "z")

    def test_shortener_accepts_md5(self):
        s = URLShortener(strategy=md5_hash)
        short = s.shorten("https://example.com")
        self.assertEqual(s.expand(short), "https://example.com")
        # idempotent — same long URL returns same short
        self.assertEqual(s.shorten("https://example.com"), short)


class TestConcurrency(unittest.TestCase):
    def test_concurrent_shorten_is_idempotent(self):
        """Many threads shortening the same URL must all get the same short."""
        s = URLShortener()
        long_url = "https://example.com"

        with ThreadPoolExecutor(max_workers=8) as ex:
            results = list(ex.map(lambda _: s.shorten(long_url), range(100)))

        self.assertEqual(len(set(results)), 1)  # all identical
        self.assertEqual(len(s), 1)  # only one mapping created

    def test_concurrent_shorten_distinct_urls_no_collisions(self):
        """Different URLs shortened concurrently must each get distinct shorts."""
        s = URLShortener()

        with ThreadPoolExecutor(max_workers=8) as ex:
            results = list(
                ex.map(lambda i: s.shorten(f"https://example.com/{i}"), range(200))
            )

        self.assertEqual(len(set(results)), 200)
        self.assertEqual(len(s), 200)

    def test_concurrent_expand_under_shorten(self):
        """expand() must keep working while another thread is shortening."""
        s = URLShortener()
        long_url = "https://seed.com"
        seed = s.shorten(long_url)

        def shortener() -> None:
            for i in range(500):
                s.shorten(f"https://example.com/{i}")

        def expander() -> None:
            for _ in range(500):
                self.assertEqual(s.expand(seed), long_url)

        with ThreadPoolExecutor(max_workers=2) as ex:
            f1 = ex.submit(shortener)
            f2 = ex.submit(expander)
            f1.result()
            f2.result()  # re-raises if either thread raised


if __name__ == "__main__":
    unittest.main()
