import threading

from strategies import Counter, Strategy


class UnknownShortURLError(KeyError):
    """Raised when expand() is called with a short URL that was never shortened."""


class CollisionError(RuntimeError):
    """Raised when a generated short URL already maps to a different long URL."""


class URLShortener:
    """Bidirectional long↔short URL mapper with a pluggable generation strategy.

    All operations are thread-safe. `shorten` is idempotent: the same long URL
    always returns the same short URL. The strategy is responsible for *how*
    the short URL is generated; the shortener is responsible for storing the
    mapping and detecting collisions.
    """

    def __init__(self, strategy: Strategy | None = None) -> None:
        self._strategy: Strategy = strategy or Counter()
        self._long_to_short: dict[str, str] = {}
        self._short_to_long: dict[str, str] = {}
        self._lock = threading.Lock()

    def shorten(self, long_url: str) -> str:
        """Return the short URL for `long_url`, generating one if needed.

        Idempotent — repeated calls with the same `long_url` return the same short.
        Raises CollisionError if the strategy returns a short already bound to a
        different long_url.
        """
        with self._lock:
            if existing := self._long_to_short.get(long_url):
                return existing

            short = self._strategy(long_url)
            collision = self._short_to_long.get(short)
            if collision is not None and collision != long_url:
                raise CollisionError(
                    f"short {short!r} already maps to {collision!r}"
                )

            self._long_to_short[long_url] = short
            self._short_to_long[short] = long_url
            return short

    def expand(self, short_url: str) -> str:
        """Return the long URL for `short_url`. Raises UnknownShortURLError if not found."""
        with self._lock:
            try:
                return self._short_to_long[short_url]
            except KeyError:
                raise UnknownShortURLError(short_url) from None

    def __len__(self) -> int:
        with self._lock:
            return len(self._long_to_short)

    def __contains__(self, long_url: object) -> bool:
        with self._lock:
            return long_url in self._long_to_short
