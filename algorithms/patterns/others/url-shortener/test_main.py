import unittest
from concurrent.futures import ThreadPoolExecutor

from main import (
    CollisionError,
    UnknownShortURLError,
    URLShortener,
)


class TestURLShortener(unittest.TestCase):
    def test_round_trip(self):
        s = URLShortener()
        short = s.shorten("https://example.com")
        self.assertEqual(s.expand(short), "https://example.com")

    def test_shorten_is_idempotent(self):
        s = URLShortener()
        a = s.shorten("https://example.com")
        b = s.shorten("https://example.com")
        self.assertEqual(a, b)

    def test_distinct_urls_get_distinct_shorts(self):
        s = URLShortener()
        a = s.shorten("https://example.com")
        b = s.shorten("https://other.com")
        self.assertNotEqual(a, b)

    def test_expand_unknown_raises(self):
        s = URLShortener()
        with self.assertRaises(UnknownShortURLError):
            s.expand("nope")

    def test_collision_raises(self):
        s = URLShortener(strategy=lambda _: "fixed")
        s.shorten("https://example.com")
        with self.assertRaises(CollisionError):
            s.shorten("https://other.com")

    def test_concurrent_shorten_distinct_urls(self):
        s = URLShortener()
        with ThreadPoolExecutor(max_workers=8) as ex:
            shorts = list(ex.map(lambda i: s.shorten(f"https://ex.com/{i}"), range(200)))
        self.assertEqual(len(set(shorts)), 200)


if __name__ == "__main__":
    unittest.main()
