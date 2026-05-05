# URL Shortener

Common Revolut / system-design coding problem (mentioned across multiple Glassdoor reviews). Builds a TinyURL-style service: long URL → short token, then back.

## Stage 1 — Basic operations

- `shorten(long_url: str) -> str` — generate a short URL for `long_url`. Idempotent: same input always returns the same short.
- `expand(short_url: str) -> str` — return the long URL for a previously-shortened token. Raise if not found.

## Stage 2 — Pluggable generation strategies

Make the *how-to-generate* interchangeable. Common candidates:

- **Counter** — monotonic int (`1`, `2`, …). Stateful, ignores `long_url`.
- **MD5 hash** — first 8 hex chars of `md5(long_url)`. Deterministic.
- **Base64** — first 8 chars of `urlsafe_b64encode(long_url)`. Deterministic.
- **Random string** — random alphanumeric. Non-deterministic.

The shortener owns the storage; strategies just generate. The shortener detects collisions (same short token bound to a different long URL).

## Stage 3 — Concurrency

`shorten` / `expand` must be safe to call from multiple threads. Idempotence must hold under concurrent shortens of the same URL.

## Examples

### Example 1 — idempotent

```text
s = URLShortener(Counter())
s.shorten("https://example.com")   # "1"
s.shorten("https://example.com")   # "1"  (same)
s.shorten("https://other.com")     # "2"
```

### Example 2 — round-trip

```text
short = s.shorten("https://example.com")
s.expand(short)                    # "https://example.com"
```

### Example 3 — unknown short

```text
s.expand("does-not-exist")         # raises UnknownShortURLError
```

### Example 4 — collision

```text
# strategy that always returns the same short
s = URLShortener(strategy=lambda _: "abc")
s.shorten("https://a.com")         # "abc"
s.shorten("https://b.com")         # raises CollisionError
```

---

## How to lead the interview (5-phase script)

### Phase 1 — Understand (3-5 min)

1. *"Should `shorten(same_url)` always return the same short, or generate a fresh one?"* → idempotent
2. *"What's the format of a short URL — any string, fixed length, alphanumeric only?"* → string of fixed length
3. *"What happens if two different long URLs hash to the same short?"* → raise CollisionError
4. *"What happens on `expand` for an unknown short?"* → raise UnknownShortURLError
5. *"Single-threaded or concurrent?"* → concurrent
6. *"Should we validate URLs?"* → no — that's the API boundary's job
7. *"Strategy fixed at construction or pluggable?"* → expect *"start with one, we'll discuss more"*

### Phase 2 — Plan (3-5 min)

> *"I'll keep a bidirectional map: `dict[long → short]` and `dict[short → long]`. The first gives idempotence (`if long in map → return cached short`). The second gives O(1) `expand` and lets me detect collisions before committing.*
>
> *Strategies are callables matching `Callable[[str], str]` — function for stateless ones (md5, base64, random), class with `__call__` for stateful (counter). Default to counter.*
>
> *Single `threading.Lock` guards both dicts. `shorten` and `expand` are O(1).*
>
> *Tests: idempotence, round-trip, unknown expand, collision, concurrency."*

### Phase 3 — Code (15-20 min)

Build incrementally:

1. `Strategy = Callable[[str], str]` type alias.
2. `Counter` class with internal lock.
3. `md5_hash` / `base64_hash` / `random_string` as functions.
4. `URLShortener` with the two dicts + lock.
5. `shorten` (idempotence first, then collision check, then commit).
6. `expand` raising `UnknownShortURLError`.
7. Add asserts inline.

### Phase 4 — Test (5-8 min)

Walk through:

- shorten same URL twice → identical
- two distinct URLs → distinct shorts
- expand round-trip
- expand unknown → raises
- collision via mock strategy → raises
- concurrent same-URL shorten → all get the same value (idempotence holds under contention)

**Find at least one bug yourself.**

### Phase 5 — Reflect & optimise (2-3 min)

> *"For production: persistence (Redis / Postgres), TTL on entries, per-user quotas, sharding by short-prefix, monotonic IDs encoded in base62 to keep shorts small (`1` → `b`, `26` → `B`, etc.). Collision retry: with random/hash strategies, on collision retry up to N attempts before giving up. The single lock is fine until you're handling >10k req/s — then split per-shard or use a CAS-based approach on a concurrent map."*

---

## Likely follow-ups (rehearse one-liners)

| extension | one-line answer |
| --- | --- |
| **Custom alphabet / shorter shorts** | base62 encode the counter (62 chars vs 36/16); fits trillions in 7 chars |
| **TTL / expiry** | store `(long_url, expires_at)`; lazy-evict on `expand`; or background sweep |
| **Per-user quotas** | dict `{user_id: count}`; check before `shorten` |
| **Custom alias (vanity URL)** | `shorten(long_url, alias=...)`; check alias not in `_short_to_long` first |
| **Hit counter / analytics** | `dict[short, int]`; increment in `expand`; or off-host (statsd, Kafka) |
| **Persistence** | swap in-memory dicts for Redis (`SETNX` for atomicity) or Postgres (UNIQUE constraint) |
| **Sharding** | hash short URL → shard ID; route reads/writes to that shard |
| **Collision-retry strategy** | wrap a strategy in `retry(strategy, max_attempts=5)` decorator |

---

## Common pitfalls to avoid

- **Don't put validation regex inside the shortener.** URL validation is a separate concern — rejection should happen at the API layer.
- **Don't forget the collision case** when the strategy is non-deterministic. A naive `_short_to_long[short] = long_url` silently overwrites a previous mapping.
- **Don't forget idempotence** under concurrency. Two threads calling `shorten(same_url)` simultaneously must both return the same short — this is what the lock guarantees.
- **Don't conflate "URL not found" with empty / None.** Raise an explicit error so callers can't accidentally use `None` as a real URL.
- **Don't compute the short while holding the lock for slow strategies.** If a strategy ever does I/O (database, network), follow the load-balancer pattern: snapshot inputs under lock, compute outside, commit under lock again.

---

## Project layout

Flat — no package, just files in one directory:

```text
url-shortener/
├── pyproject.toml             # uv config, non-package mode
├── uv.lock
├── .python-version
├── url-shortener.md
├── shortener.py               # URLShortener + UnknownShortURLError + CollisionError
├── strategies.py              # Strategy type + Counter + md5_hash + base64_hash + random_string
├── test_shortener.py
├── test_strategies.py
└── test_concurrency.py
```

### Run

```sh
uv sync
uv run pytest
```

### Note for the live interview

In 40 minutes, **everything goes in one file** with `assert` tests under `if __name__ == "__main__":`. The split here is what to *talk about* during Phase 5 ("how I'd organise it for production").
