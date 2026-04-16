# Concurrency in Distributed Systems

When multiple instances operate on shared state simultaneously, two core problems arise:

- **Race condition** — concurrent read-modify-write on the same resource; one operation silently overwrites the other
- **Double processing** — the same event or message is processed more than once (e.g. after a retry)

## Strategies

- **[Locking](locking.md)** — one writer at a time via optimistic or pessimistic locks
- **[Idempotence](idempotence.md)** — safe retries; executing the same operation multiple times produces the same result
