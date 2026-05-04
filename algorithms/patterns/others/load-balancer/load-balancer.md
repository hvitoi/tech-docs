# Load Balancer

Implement an in-memory `LoadBalancer` that distributes requests across a pool of backend servers.

## Stage 1 — Basic operations

- `register(server: str) -> bool` — add a server. Return `True` if added, `False` if already present or the pool is full.
- `unregister(server: str) -> bool` — remove a server. Return `True` if removed, `False` if not present.
- `get() -> str` — pick a server to handle the next request. Raise if no servers are registered.
- The pool has a maximum capacity, e.g. `10`.

## Stage 2 — Pluggable selection strategies

Make the picking logic interchangeable. Start with **round-robin**, then add **random**.

Likely follow-ups: weighted random, least-connections, sticky sessions.

## Stage 3 — Concurrency

The load balancer must be safe to call from multiple threads. Mutations and reads should not race.

## Examples

### Example 1 — round-robin

```text
lb = LoadBalancer(strategy=RoundRobinStrategy())
lb.register("a")
lb.register("b")
lb.register("c")

[lb.get() for _ in range(7)]   # ["a","b","c","a","b","c","a"]
```

### Example 2 — full pool / duplicate

```text
lb = LoadBalancer(max_servers=2)
lb.register("a")  # True
lb.register("a")  # False  (duplicate)
lb.register("b")  # True
lb.register("c")  # False  (full)
```

### Example 3 — empty pool

```text
lb = LoadBalancer()
lb.get()   # raises NoServersAvailableError
```

---

## How to lead the interview (5-phase script)

### Phase 1 — Understand (3-5 min, **don't skip**)

Restate the problem in your own words, then ask:

1. *"What's the format of a server — string ID/URL, or a structured object?"* → string
2. *"Should servers be unique in the pool?"* → yes
3. *"On `register` of a duplicate: return `False`, raise, or silently succeed?"* → return `False`
4. *"On `get()` with empty pool — raise, return `None`, or block?"* → raise
5. *"Single-threaded or concurrent callers?"* → concurrent (almost always for this problem)
6. *"Strategy fixed at construction or pluggable?"* → expect *"start with round-robin, we'll discuss more"*
7. *"Max pool size?"* → fixed at construction, default 10

If they say "you decide", state your assumption out loud: *"I'll assume X — let me know if you want different behaviour."*

### Phase 2 — Plan (3-5 min)

Speak the entire rubric in 30 seconds **before typing a line**:

> *"I'll use the Strategy pattern — `LoadBalancer` holds a `Strategy` that picks a server from the current pool. Round-robin needs internal state (an index), so the strategy is stateful. I'll inject the strategy via the constructor; default round-robin.*
>
> *For thread safety, a `threading.Lock` guarding the pool. Pool is `list[str]` because order matters for round-robin. `register` is O(1) amortised, `unregister` is O(n) (`list.remove`), `get` is O(1).*
>
> *Tests will cover empty/full pool, duplicate register, unregister-not-present, round-robin cycling, random distribution.*
>
> *Is this OK or should I aim for something else upfront?"*

Wait for the nod.

### Phase 3 — Code (15-20 min)

Build incrementally. Narrate each piece:

1. Strategy interface (ABC).
2. `RoundRobinStrategy`.
3. `LoadBalancer` with `register` / `unregister` / `get`.
4. Add the `Lock`.
5. Add `RandomStrategy` once they ask for it.
6. Drop in asserts as you write — don't batch them at the end.

### Phase 4 — Test (5-8 min)

Run through:

- empty pool → `get()` raises
- full pool → 11th `register` returns `False`
- duplicate → second `register("a")` returns `False`
- round-robin → 4 calls on `[a,b,c]` → `[a,b,c,a]`
- random → returns a member of the pool

**Find one bug yourself** — say it out loud, fix it. It's graded on this.

### Phase 5 — Reflect & optimise (2-3 min)

> *"For production: weighted round-robin (prefix sums + bisect, O(log n)), least-connections (track in-flight per server), health checks (background pings, exclude unhealthy), sticky sessions (hash by client ID). Lock could become a bottleneck under high `get()` load — copy-on-write list with atomic reference swap would let `get()` be lock-free."*

That single paragraph signals senior-level awareness.

---

## Likely follow-ups (rehearse one-liners)

| extension | one-line answer | sketch |
| --- | --- | --- |
| **Weighted random** | "prefix sums + bisect" | `cum[i] = sum(weights[:i+1])`; `r = random.uniform(0, total)`; `bisect_left(cum, r)` → O(log n) |
| **Least connections** | "track in-flight count per server, pick min" | dict `{server: count}`; argmin in O(n), or heap for O(log n); caller calls `done(server)` to decrement |
| **Sticky sessions** | "hash client ID modulo pool size" | `pool[hash(client_id) % len(pool)]`; doesn't survive resize without consistent hashing |
| **Health checks** | "background task pings each server every k s; mark dead, exclude" | maintain `_healthy: set[str]`; selection uses intersection |
| **Lock-free `get()`** | "copy-on-write list, atomic reference swap" | mutations build new list; CPython single-assignment is atomic; readers grab a reference once |
| **Distributed** | "consistent hashing or service discovery (Consul, etcd, k8s endpoints)" | push routing to the proxy (Envoy, NGINX) and let k8s manage pool membership |

---

## Common pitfalls to avoid

- **Don't put the pool inside the strategy.** The strategy receives a snapshot; this keeps it reusable.
- **Don't forget the empty-pool case** — interviewers always test it.
- **Don't hold the lock while calling user code** (e.g. `strategy.select`). Snapshot first, select outside.
- **Don't use `set` for the pool** if you have round-robin — order matters.
- **Don't ignore that `list.remove` is O(n)** — state it. If pushed, switch to `dict[server → index]` for O(1) removal.
- **Don't write tests after coding** — write a couple of asserts as you go.

---

## Mental cheatsheet (pin to monitor)

```text
1. Clarify (3 min)  unique? full? empty get raises? thread-safe? max_servers?
2. Plan   (3 min)   Strategy pattern, list+lock, ABC, default round-robin
3. Code   (15-20)   ABC → RR → LB(register/unregister/get) → Lock → Random
4. Test   (5-8)     empty, full, duplicate, RR cycle, post-unregister
5. Reflect (3)      weighted, least-conn, health checks, lock-free
```

### Project Layout

You wouldn't actually build this whole layout in 40 minutes — for the interview, **everything goes in one file** and tests live under `if __name__ == "__main__":`. The split shown here is what a senior engineer would point to as "this is what I'd do if I had more time" — useful talking material in Phase 5 (Reflect).
