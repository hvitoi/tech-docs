# Event Sourcing

> Event Sourcing is a pattern where changes to the application state are stored as a sequence of events. Instead of storing just the current state of data in a domain, Event Sourcing stores a log of all the changes (events) that have occurred over time. This allows the application to reconstruct past states and provides an audit trail of changes. Event Sourcing is beneficial in scenarios requiring complex business transactions, auditability, and the ability to rollback or replay events.

- Store all the events related to an entity as a `sequence of events`
- This way, the information is `append only`
- These events must be stored in another database in the exact order that they were applied

## Querying information

- Whenever the final value needs to be retrieved, simply apply all the vents (relative to that entity) in order
- We can make the query faster by creating `snapshot events` and thus avoid having to apply all the events from the very beginning
- We can choose how long to retain old events (e.g., 10 years). In the case older events are dropped, a snapshot has to be created before

## Implementations

- `Datomic` is a implementation of append only transaction-driven database
