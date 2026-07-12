# Event Sourcing

Instead of storing current state, store the full sequence of state-changing `events`. Current state is derived by replaying events, not read directly.

- The event log is the `source of truth` — a row in a table is just a cached projection of it
- Append-only — events are immutable, only ever appended, never updated or deleted

## Benefits

- **Full audit trail** — every change is recorded, with what happened and when
- **Time travel** — rebuild state as of any point in time by replaying up to that event
- **Rebuild projections** — fix a bug in a read model by replaying events into a new one

## Trade-offs

- **Replay cost** — long streams get slow to rebuild from; mitigated with periodic `snapshots`
- **Schema evolution** — old events must stay readable as the event shape changes over time (upcasting)
- **Eventual consistency** — projections built from events usually lag behind the event log

## Related

- Pairs naturally with **[CQRS](cqrs.md)** — events are the write model, projections are the read model
- Often published via a **[transactional outbox](transactional-outbox.md)** to keep the write and the publish atomic
