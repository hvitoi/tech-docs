# Transactional Outbox

Problem: a service needs to update its own database AND publish an event about that change — but a DB write and a broker publish can't share one transaction (the `dual write problem`). If the commit succeeds and the publish fails (or vice versa), the two systems drift out of sync.

## The Solution

- Write the event to an `outbox` table, in the same local transaction as the business data change
- A separate process reads the outbox table and publishes to the broker, then marks the row as sent
  - **Polling publisher** — a worker polls the outbox table on an interval
  - **Change Data Capture (CDC)** — a tool (e.g. Debezium) tails the DB transaction log and publishes new rows automatically

## Guarantees

- The business change and the outbox row commit atomically — either both happen or neither does
- Delivery to the broker is `at-least-once` — pair it with an **[idempotent](idempotency.md)** consumer to handle duplicates

## Trade-offs

- Extra table and publishing process to operate
- Consumers see the event slightly after the write commits, not synchronously
