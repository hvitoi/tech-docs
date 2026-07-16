# Durability

- Once a transaction is committed, its changes are **permanent** — they survive crashes, power failures, and restarts
- Implemented via **write-ahead logging (WAL)**: changes are written to a persistent log *before* being applied to the data files
- On recovery, the database replays the WAL to restore committed transactions that weren't yet flushed to disk
