# Reconcile

Reconciliation is the core control loop pattern in Kubernetes: compare `desired state` (manifest spec) against `actual state` (cluster reality) and take actions to make them match.

## Level-triggered vs edge-triggered

Reconciliation is **level-triggered**: it reacts to the current state, not just the event that triggered it. This means:

- Missed events don't cause permanent inconsistency — the next reconcile corrects it
- The function must be **idempotent**: running it multiple times produces the same result
- On failure, simply requeue — no need to track what partially happened

This is more resilient than imperative, edge-triggered approaches.

## Key properties

- **Idempotent** — safe to run repeatedly
- **Self-healing** — drift from desired state is corrected automatically
- **Eventually consistent** — the system converges, not necessarily immediately
- **Optimistic** — assumes things usually work; retries on failure
