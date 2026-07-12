# Message Deduplication

Queues/topics typically guarantee `at-least-once` delivery — retries mean the same message can arrive more than once. Consumers must handle duplicates explicitly.

## Delivery semantics

- **At-most-once** — delivered 0 or 1 times; no retries, so no duplicates, but messages can be lost
- **At-least-once** — retried until acknowledged; guarantees delivery, but can duplicate (the common default)
- **Exactly-once** — no loss, no duplicates; hardest to achieve, requires coordination across producer + broker + consumer (e.g. Kafka transactions)

## Techniques

Duplicates can be introduced on either side of the broker, and each side needs its own defense:

- **Idempotent producer**
  - Producer attaches a dedup ID per logical message
  - The broker rejects a repeat publish seen within a time window (e.g. SQS FIFO `MessageDeduplicationId`, Azure Service Bus duplicate detection)
  - This only guards against the producer resending — it does nothing for duplicates introduced further downstream

- **Idempotent consumer**
  - The broker can still deliver the same message more than once (e.g. consumer crashes after processing but before committing its offset/ack). Kafka, for instance, has no broker-side redelivery dedup at all, the consumer must handle it.
  - `Check dedup ID`: the consumer must track processed message IDs itself (e.g. a processed_messages table or a Redis set) and skip ones already seen
  - `Conditional writes`: Instead of checking-then-writing, let the datastore reject the duplicate itself (e.g. a unique constraint on the message ID) — closes the race between the check and the write
  - `Content-based hash`: hash the message body when there's no natural ID, and dedup on the hash (only safe if a duplicate payload always means a duplicate message)
