# Event Sourcing

- Store all the events related to an entity as a `sequence of events`
- This way, the information is `append only`

## Querying information

- Whenever the final value needs to be retrieved, simply apply all the vents (relative to that entity) in order
- We can make the query faster by creating `snapshot events` and thus avoid having to apply all the events from the very beginning
- We can choose how long to retain old events (e.g., 10 years). In the case older events are dropped, a snapshot has to be created before

## Implementations

- `Datomic` is a implementation of append only transaction-driven database