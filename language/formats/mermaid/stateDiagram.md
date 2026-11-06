# State Diagram

```mermaid
stateDiagram-v2
  direction LR

  [*] --> Draft
  Draft --> Submitted: submit
  Submitted --> Approved: approve
  Submitted --> Rejected: reject
  Rejected --> Draft: edit
  Approved --> Published: publish
  Published --> Published: update
  Published --> [*]

  note right of Submitted: waiting for review
```

## Syntax

- `[*] --> A`: start state
- `A --> [*]`: end state
- `A --> B`: transition
- `A --> B: event`: transition with a label
- `A --> A: event`: self-transition
- `note right of A: text`: note (`left of` also works)

## Directions

- `direction LR`: left-to-right
- `direction TB`: top-to-bottom (default)

## Composite states

```mermaid
stateDiagram-v2
  [*] --> Active

  state Active {
    [*] --> Idle
    Idle --> Running: start
    Running --> Idle: stop
  }

  Active --> [*]: shutdown
```

## Choice

```mermaid
stateDiagram-v2
  state check <<choice>>

  [*] --> check
  check --> Valid: input ok
  check --> Invalid: input bad
```
