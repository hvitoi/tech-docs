# CQRS (Command Query Responsibility Segregation)

Split the model used to `write` data (commands) from the model used to `read` data (queries), instead of one model serving both.

- **Command side** — validates and applies state changes; optimized for consistency
- **Query side** — one or more `read models` (projections), denormalized and optimized for the specific queries the app needs

## Why

- Read and write workloads often have very different shapes and scaling needs (e.g. 100x more reads than writes)
- Lets each side scale independently, and even use different storage technology

## Trade-offs

- **Eventual consistency** — the read model lags behind the write model until it catches up
- **More moving parts** — two models (often two data stores) to keep in sync instead of one

## Related

- Commonly paired with **[event sourcing](event-sourcing.md)** — the write model appends events, and read models are projections built by consuming them
