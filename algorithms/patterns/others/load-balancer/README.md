# Load Balancer

Implement an in-memory `LoadBalancer` that distributes requests across a pool of backend servers

## Stage 1 - Clarify Requirements

- "A LoadBalancer, in-memory, that takes a request and route it to the appropriate host, that will be picked up from a pool of hosts"
- It has state, implement it as a class with a couple of methods and attributes

- **targets** (A)
  - What is the format of a target? String?
  - Maximum capacity?
  - default capacity?

- **register** (M)
  - Register a duplicate: throw or false?
  - Register on max capacity: throw or false?

- **pick** (M)
  - what strategy to use to decide which server to pick? Random?
  - The strategy is plugged via constructor?
  - On Empty servers: throw?

- Handle concurrency issues and race conditions here from multiple threads?
  - Specially on the register and pick operations

> I'll use the Strategy pattern — `LoadBalancer` holds a `Strategy` that picks a server from the current pool. Round-robin needs internal state (an index), so the strategy is stateful. I'll inject the strategy via the constructor; default round-robin.
> For thread safety, a `threading.Lock` guarding the pool. Pool is `list[str]` because order matters for round-robin. `register` is O(1) amortised, `unregister` is O(n) (`list.remove`), `get` is O(1).

## Stage 2 — Class Skeleton and simple methods

- Sketch the class skeleton and its constructors and methods
- Develop simple tests for each method before coding it, and more tests to enrich it along the implementation

## Stage 3 — Strategies

Make the picking logic interchangeable

Likely follow-ups: weighted random, least-connections, sticky sessions.

## Stage 4 — Concurrency

The load balancer must be safe to call from multiple threads. Mutations and reads should not race.

## Phase 5 — Reflect & optimise

- **Sticky sessions**: hash client ID modulo pool size. `pool[hash(client_id) % len(pool)]`; doesn't survive resize without consistent hashing

- **Health checks**: background task pings each server every X seconds; mark dead, exclude"

- **Lock-free pick()**: copy-on-write list, atomic reference swap

- **Distributed**: consistent hashing or service discovery (Consul, etcd, k8s endpoints)

- **Other strategies**: weighted round-robin (prefix sums + bisect), least-connections (track in-flight per server with a heap),
