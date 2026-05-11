# Load Balancer

Implement an in-memory `LoadBalancer` that distributes requests across a pool of backend servers

## Stage 1 - Clarify Requirements

- "A LoadBalancer, in-memory, that takes a request and route it to the appropriate host, that will be picked up from a pool of hosts"
- It has state, implement it as a class with a couple of methods and attributes: `register` method, `pick` method, `targets` attribute
  - `targets`: What is the format of a target? A string representing the endpoint? maximum capacity, default capacity?
  - `register`: what to do when i try to register a duplicate target? Return false or throw on max capacity?
  - `pick`: what policy to use to decide which server to pick? Random? Raise when not found?
- Handle concurrency issues and race conditions here from multiple threads?
  - Specially on the register and pick operations

> *"I'll use the Strategy pattern — `LoadBalancer` holds a `Strategy` that picks a server from the current pool. Round-robin needs internal state (an index), so the strategy is stateful. I'll inject the strategy via the constructor; default round-robin.*
>
> *For thread safety, a `threading.Lock` guarding the pool. Pool is `list[str]` because order matters for round-robin. `register` is O(1) amortised, `unregister` is O(n) (`list.remove`), `get` is O(1).*
>
> *Tests will cover empty/full pool, duplicate register, unregister-not-present, round-robin cycling, random distribution.*
>
> *Is this OK or should I aim for something else upfront?"*

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
