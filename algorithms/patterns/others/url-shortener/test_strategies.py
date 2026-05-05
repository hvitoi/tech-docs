from shortener import URLShortener
from strategies import Counter, base64_hash, md5_hash, random_string


# --- counter ---


def test_counter_increments_per_call():
    c = Counter()
    assert [c("any") for _ in range(3)] == ["1", "2", "3"]


def test_counter_ignores_long_url():
    c = Counter()
    a = c("https://example.com")
    b = c("https://other.com")
    assert int(b) == int(a) + 1


# --- md5 ---


def test_md5_is_deterministic():
    assert md5_hash("https://example.com") == md5_hash("https://example.com")


def test_md5_distinct_inputs_distinct_shorts():
    assert md5_hash("https://a.com") != md5_hash("https://b.com")


def test_md5_short_length_is_8():
    assert len(md5_hash("https://example.com")) == 8


# --- base64 ---


def test_base64_is_deterministic():
    assert base64_hash("https://example.com") == base64_hash("https://example.com")


def test_base64_short_length_is_8():
    assert len(base64_hash("https://example.com")) == 8


# --- random ---


def test_random_string_length_is_8():
    assert len(random_string("anything")) == 8


def test_random_string_is_non_deterministic():
    """Two calls should differ — astronomically unlikely otherwise."""
    seen = {random_string("anything") for _ in range(100)}
    assert len(seen) > 1


# --- strategy injection through URLShortener ---


def test_shortener_accepts_arbitrary_callable_strategy():
    """A `Strategy` is just a callable — anything matching the signature works."""
    counter = iter("xyz")
    s = URLShortener(strategy=lambda _: next(counter))
    assert s.shorten("https://a.com") == "x"
    assert s.shorten("https://b.com") == "y"
    assert s.shorten("https://c.com") == "z"


def test_shortener_accepts_md5():
    s = URLShortener(strategy=md5_hash)
    short = s.shorten("https://example.com")
    assert s.expand(short) == "https://example.com"
    # idempotent — same long URL returns same short
    assert s.shorten("https://example.com") == short
