# WAL (Write-Ahead Log)

- Before PG changes any data on disk, first it writes the change to an `append-only log` (the WAL)
- If the server crashes, PG replays the WAL on startup to recover any committed changes that handn't yet made into the data files
- Every byte written to that log has an address called the `Log Sequence Number` (LSN) — literally the offset into the logical WAL stream
