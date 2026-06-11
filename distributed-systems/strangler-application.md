# Strangler Application Pattern

- A strategy for migrating a legacy system to a new system incrementally, avoiding a risky "big bang" rewrite with a high-risk cutover
- Named after the strangler fig vine, which grows around a tree and gradually replaces it.

## The Solution

- Incrementally build a new application (the "strangler") *around* the existing system
- New functionality and migrated functionality live in the new system, while the legacy keeps shrinking until it can be retired.

## How It Works

The strangler application is made up of two kinds of services:

- **Replacement services** — take over functionality previously handled by the monolith.
- **New feature services** — add brand-new capabilities.

- A routing/proxy layer sits in front, directing each request either to the legacy or to the new services
- Over time, the services absorb the monolith's responsibilities until the legacy system is "strangled" and decommissioned.

## Benefits

- **Lower risk** — incremental migration instead of one massive cutover.
- **Continuous delivery of value** — the application stays deployable throughout.
- **Business buy-in** — new-feature services demonstrate the value of microservices early, helping justify the effort.

## Drawbacks / Considerations

- Both the old and new systems must run and be maintained in parallel during the transition.
- Requires a routing mechanism, adding operational complexity.

## Related Patterns

- **Anti-Corruption Layer** — insulates new services from the monolith's data model.
- **Monolith-to-microservices refactoring** — the broader approach this fits into.

## Reference

- <https://microservices.io/patterns/refactoring/strangler-application.html>
