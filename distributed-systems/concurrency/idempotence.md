# Idempotence

An operation is idempotent if executing it multiple times produces the same result as executing it once.

## Techniques

- **Message deduplication** — track processed message IDs; discard duplicates before processing
- **Conditional writes** — use unique keys or version checks so repeated writes are no-ops (e.g. `INSERT ... ON CONFLICT DO NOTHING`)
- **Exactly-once semantics** — the messaging system itself guarantees no duplicates (requires producer + broker + consumer coordination)
- **Dead-letter queue (DLQ)** — messages that repeatedly fail are moved aside instead of retried indefinitely
