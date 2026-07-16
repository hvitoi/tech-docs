# Data modeling

- Table for `Actors`
- E.g., store, customer, seller

- Table for `Actions` of actors
- E.g., customers make orders, complains, returns

- Table for `properties of actors` that don’t fit to 2D diagram
- E.g., possible payment methods for customer

- Table for `properties of actions` that don’t fit to 2D diagram
- E.g., possible reasons for return

## Redundancy: one copy, or many?

Every paradigm faces the same decision — store each fact **once and reference it**, or **duplicate it** so a single read returns everything:

| | One copy | Duplicated |
| --- | --- | --- |
| Relational | normalized, JOIN on read | denormalized, wide tables |
| Document | referencing (`$lookup`) | embedding |
| Wide-column | (avoided) | duplicate per query pattern |

- Cheap writes and no drift vs. cheap reads and no joins — you cannot have both
- The rule of thumb is to model for the **read pattern**: normalize until it hurts, denormalize until it works
- Duplicating means every copy must be updated together, which is where consistency bugs live
- The relational theory behind this (normal forms, update anomalies) is in [types/relational/9.normalization.md](types/relational/9.normalization.md)
- Which side a workload lands on is largely decided by `OLTP` vs `OLAP` — see [oltp-olap.md](oltp-olap.md)
