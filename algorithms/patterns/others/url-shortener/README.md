# URL Shortener

## Clarify requirements

- "A URL shortener, that takes a long-form url and transform into a short format, and can expand it after"
- It has a state, the mapping between the short and long, and methods: `shorten` and `expand`

- **shorten**
  - What is the strategy to shorten (counter, md5, base64, random)
  - Is the strategy fixed or pluggable?
  - How to handle collisions? What happens if two different long URLs have the same short? Throw (if strategy is deterministic) or retry (if strategy is non-deterministic)?
  - Should it be idempotent? Same input -> same output?
  - What is the format of the short url? fixed length?
  - Validate the URLs first?

- **expand**
  - Throw if not found?

- Handle concurrency issues and race conditions here from multiple threads?

> I'll keep a bidirectional map: `dict[long → short]` and `dict[short → long]`. The first gives idempotence, The second gives O(1) `expand` and lets me detect collisions before committing.
> Strategies are callables matching `Callable[[str], str]` — function for stateless ones (md5, base64, random), class with `__call__` for stateful (counter). Default to counter.

### Reflect & optimise

For production: persistence (Redis / Postgres), TTL on entries, per-user quotas, sharding by short-prefix, monotonic IDs encoded in base62 to keep shorts small. With random/hash strategies, retry up to N attempts on collision before giving up. The single lock is fine until you're handling >10k req/s — then split per-shard or use a CAS-based approach on a concurrent map

- **TTL**: "store `(long_url, expires_at)` with a background sweep
- **Hit counter / analytics** `dict[short, int]` increment in `expand`
- **Collision-retry strategy**: wrap a strategy in `retry(strategy, max_attempts=5)` useful for random/hash strategies
- **Persistence**: swap in-memory dicts for Redis (`SETNX`) or Postgres (UNIQUE constraint) - DB enforces idempotence + collision
- **Sharding**: hash short URL → shard ID; route reads/writes to that shard"
