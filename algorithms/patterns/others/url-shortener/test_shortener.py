import pytest

from shortener import (
    CollisionError,
    UnknownShortURLError,
    URLShortener,
)
from strategies import Counter


def test_shorten_is_idempotent():
    s = URLShortener(Counter())
    a = s.shorten("https://example.com")
    b = s.shorten("https://example.com")
    assert a == b
    assert len(s) == 1


def test_distinct_urls_get_distinct_shorts():
    s = URLShortener(Counter())
    a = s.shorten("https://example.com")
    b = s.shorten("https://other.com")
    assert a != b
    assert len(s) == 2


def test_expand_round_trip():
    s = URLShortener(Counter())
    short = s.shorten("https://example.com")
    assert s.expand(short) == "https://example.com"


def test_expand_unknown_raises():
    s = URLShortener(Counter())
    with pytest.raises(UnknownShortURLError):
        s.expand("nope")


def test_collision_with_different_long_url_raises():
    """A strategy that returns a short already mapped to a different long URL must raise."""

    def always_collides(_: str) -> str:
        return "fixed-short"

    s = URLShortener(strategy=always_collides)
    s.shorten("https://example.com")
    with pytest.raises(CollisionError):
        s.shorten("https://other.com")


def test_default_strategy_is_counter():
    s = URLShortener()
    s.shorten("https://example.com")
    s.shorten("https://other.com")
    assert s.expand("1") == "https://example.com"
    assert s.expand("2") == "https://other.com"


def test_len_and_contains():
    s = URLShortener()
    assert len(s) == 0
    assert "https://example.com" not in s
    s.shorten("https://example.com")
    assert len(s) == 1
    assert "https://example.com" in s
