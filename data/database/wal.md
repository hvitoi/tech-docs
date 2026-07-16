# WAL (Write-Ahead Log)

- Universal durability technique — **not a relational concept**. Any store that must survive a crash has one under some name
- The rule: **before any change reaches the data files on disk, the change is first appended to a log**, and that log is `fsync`ed
- On crash, the engine replays the log on startup to recover committed changes that hadn't made it into the data files yet
- This is the mechanism behind [durability](acid/durability.md), the D in ACID

## Why it exists

- Writing data pages in place is **random I/O** and is not atomic (a page can tear mid-write)
- Appending to a log is **sequential I/O** and cheap to force to disk
- So a commit only has to wait for a sequential append, not for the pages themselves — pages are flushed later, lazily (`checkpointing`)
- This is what makes `COMMIT` fast *and* durable at the same time

## Vocabulary

- `Log record` — the change to be replayed, addressed by an offset/id into the log stream
- `Checkpoint` — flush dirty data pages to their real location; the log up to that point can then be recycled
- `Redo` — replay committed changes missing from the data files
- `Undo` — roll back uncommitted changes found in the log (this is how [atomicity](acid/atomicity.md) is implemented)
- `Archiving` — copying log segments elsewhere, which enables PITR and replication

## What the log unlocks (beyond crash recovery)

- `Point-in-time recovery` — restore a base backup, then replay the log up to a chosen moment
- `Replication` — ship the log to another node and let it replay; this is what streaming/physical replication *is*
- `CDC` — decode the log into a change stream (Debezium, logical decoding)
- `Consensus` — in distributed stores the replicated log **is** the database (Raft); nodes agree on log order, then apply it

## Per-engine mapping

| Engine | Name | Notes |
| --- | --- | --- |
| PostgreSQL | WAL | 16MB segments in `pg_wal/`, addressed by `LSN` (the byte offset into the log stream). `wal_level=logical` enables CDC; a stuck replication slot will fill the disk |
| MySQL / InnoDB | `redo log` + `undo log` | `ib_logfile*`; the binlog is a *separate*, logical log used for replication |
| SQLite | WAL mode | Opt-in (`PRAGMA journal_mode=WAL`); default is a `rollback journal` instead — see [types/relational/sqlite/sqlite.md](types/relational/sqlite/sqlite.md) |
| Oracle | redo log | |
| MongoDB | `journal` | WiredTiger journal; the `oplog` is the separate logical log used for replication |
| Redis | `AOF` (append-only file) | Opt-in; `RDB` snapshots are the alternative, weaker durability |
| Elasticsearch | `translog` | Per-shard, replayed on restart before segments are committed |
| etcd / Consul | Raft log | The log *is* replicated by consensus, then applied to the state machine |
| Kafka | the log | Inverts it — the log is the primary abstraction, not an implementation detail |

- Note SQLite's default is the **inverse** strategy: a rollback journal writes the *old* page contents aside, then modifies the data file in place. WAL writes the *new* content to the log and leaves the data file alone. WAL is the better one, which is why nearly everyone else uses it

## Trade-offs

- Every change is written **twice** (once to the log, once to the data files) — the durability tax, known as `write amplification`
- A commit is only as durable as the `fsync` behind it. Every engine has a knob to relax this for speed, at the cost of losing recent commits on power loss:
  - PostgreSQL `synchronous_commit`
  - MySQL `innodb_flush_log_at_trx_commit`
  - SQLite `PRAGMA synchronous`
  - MongoDB write concern `j: true`
  - Redis `appendfsync`
- The log must be checkpointed/recycled or it grows without bound — a stalled replica or a failing archive command is a classic way to fill a disk
