from concurrent.futures import ThreadPoolExecutor

from shortener import URLShortener


def test_concurrent_shorten_is_idempotent():
    """Many threads shortening the same URL must all get the same short."""
    s = URLShortener()
    long_url = "https://example.com"

    def worker() -> str:
        return s.shorten(long_url)

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(lambda _: worker(), range(100)))

    assert len(set(results)) == 1  # all identical
    assert len(s) == 1  # only one mapping created


def test_concurrent_shorten_distinct_urls_no_collisions():
    """Different URLs shortened concurrently must each get distinct shorts."""
    s = URLShortener()

    def worker(i: int) -> str:
        return s.shorten(f"https://example.com/{i}")

    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(worker, range(200)))

    assert len(set(results)) == 200
    assert len(s) == 200


def test_concurrent_expand_under_shorten():
    """expand() must keep working while another thread is shortening."""
    s = URLShortener()
    long_url = "https://seed.com"
    seed = s.shorten(long_url)

    def shortener() -> None:
        for i in range(500):
            s.shorten(f"https://example.com/{i}")

    def expander() -> None:
        for _ in range(500):
            assert s.expand(seed) == long_url

    with ThreadPoolExecutor(max_workers=2) as executor:
        f1 = executor.submit(shortener)
        f2 = executor.submit(expander)
        f1.result()
        f2.result()  # re-raises if either thread raised
