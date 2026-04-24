# Rate Limiting

- Controls the `rate of requests` a client (or tenant, IP, API key, user, etc.) can send to a system in a given time window
- Complements [backpressure](backpressure.md): backpressure protects the queue depth, rate limiting protects the arrival rate

## Why

1. `Protect` the system from overload (DoS, runaway clients, retry storms)
1. `Fair sharing` across tenants (noisy-neighbor mitigation)
1. `Cost control` (downstream APIs, compute, bandwidth)
1. `SLA enforcement` (free vs. paid tiers)

## Where to enforce

- `API Gateway` / edge proxy (coarse-grained, per-IP or per-API-key)
- `Service mesh` / sidecar (service-to-service)
- `Application code` (fine-grained, per-endpoint or per-feature)
- `Client side` (self-throttling to avoid 429s)

## Response when limit is exceeded

- `Reject` — return `429 Too Many Requests` (with `Retry-After` header)
- `Throttle / queue` — delay the request until a token is available (shaping, not policing)
- `Shed` — drop low-priority requests first (load shedding)

## Distributed rate limiting

- Counters must be shared across nodes → use `Redis` (e.g., `INCR` + `EXPIRE`, Lua scripts for atomicity)
- Trade-offs
  - `Strict` (synchronous check on every request): accurate but adds latency
  - `Eventual` (local counters, periodic sync): fast but can overshoot the limit
- For very high throughput: `sticky routing` (hash client → node) to keep counters local

---

## Algorithms

### Token Bucket

- It's the most common for API rate limiting
- Tokens are added to the bucket at a constant rate, each request `consumes` a token
- If no tokens → reject (or wait)
- Bucket has a max capacity → unused tokens accumulate up to that cap
- `Allows bursts` up to bucket capacity, then enforces the refill rate

- Parameters
  - `capacity` — max burst size
  - `refill rate` — tokens per second (the sustained rate)

- **Leaky vs. Token Bucket**
  - Leaky: smooths output, penalizes bursts (queue or drop)
  - Token: allows bursts up to capacity, then limits to sustained rate
  - Token bucket is more common for APIs (rewards idle clients with burst capacity)

### Leaky Bucket

- Models requests as water poured into a bucket with a hole at the bottom
- Water leaks out at a constant rate (the allowed throughput)
- If the bucket overflows (incoming rate > leak rate for too long), new requests are dropped
- Produces a `smooth, constant output rate` regardless of bursty input — it is a `traffic shaper`

```txt
         requests (bursty input)
              │
              ▼
         ┌─────────┐
         │         │ ← bucket capacity = max queue size
         │  ░░░░░  │
         │  ░░░░░  │
         └────┬────┘
              │     ← constant leak rate = allowed throughput
              ▼
         outgoing (smoothed)
```

- Parameters
  - `capacity` — max queued/buffered requests (burst tolerance)
  - `leak rate` — requests per second allowed out
- Properties
  - Output rate is always ≤ leak rate (hard ceiling)
  - No credit accumulation during idle periods

- Two ways to apply it:

1. **Shaper** — the bucket is a real FIFO queue; a worker processes requests at the leak rate
    - Overflow → drop. Otherwise → request waits in the queue → adds latency to the HTTP response
    - Used for traffic shaping (e.g., protect a slow downstream, packet shaping in routers)

1. **Policer** — the bucket is just a counter; "water level" leaks over time based on elapsed seconds
    - On each request: leak, then try to add 1 unit → fits = accept immediately, overflows = reject with 429
    - No queueing, no added latency — just fast accept/reject
    - More common for HTTP APIs (clients time out; they'd rather get a fast 429)

### Fixed Window Counter

- Count requests per fixed time window (e.g., 100 req / minute starting at `:00`)
- On new window → reset counter
- Simple, O(1) memory per key
- Problem: `boundary burst` — client can do 100 at `:59` and 100 at `:01`, effectively 200 in 2 seconds

### Sliding Window Counter

- Hybrid: keep fixed-window counters for current and previous window, weight by overlap
- `count ≈ prev_count * (1 - elapsed/window) + curr_count`
- Good accuracy with O(1) memory — common in practice

---

## Comparison

| Algorithm             | Bursts      | Memory | Accuracy | Output shape   |
|-----------------------|-------------|--------|----------|----------------|
| Leaky Bucket          | No (shaped) | O(N)   | Exact    | Constant rate  |
| Token Bucket          | Yes         | O(1)   | Exact    | Bursty then flat |
| Fixed Window          | Yes (edge)  | O(1)   | Loose    | Per-window cap |
| Sliding Window Counter| Yes         | O(1)   | Good     | Rolling cap    |

## Headers (HTTP convention)

- `X-RateLimit-Limit` — ceiling for the window
- `X-RateLimit-Remaining` — requests left
- `X-RateLimit-Reset` — epoch/seconds until reset
- `Retry-After` — returned with `429` to tell the client when to retry
