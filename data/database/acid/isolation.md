# Isolation

Concurrent transactions are isolated from one another — each behaves as if it were the only transaction running.

## Read Anomalies

Isolation levels exist to prevent these problems:

- **Dirty read** — reading data that another transaction hasn't committed yet (it might roll back)
- **Non-repeatable read** — reading the same row twice in one transaction and getting different values because another transaction committed in between
- **Phantom read** — running the same query twice and getting new rows because another transaction inserted them in between
- **Lost update** — two read-modify-writes race and one is silently overwritten. Note this one is *not* on the SQL standard's list, so no isolation level below Serializable is guaranteed to stop it — it's the reason `SELECT ... FOR UPDATE` exists

## Isolation Levels (least → most strict)

### Read Uncommitted

Can see uncommitted changes from other transactions. Almost never used in practice.

```sql
TX1: UPDATE accounts SET balance = 0 WHERE id = 1;  -- not committed yet
TX2: SELECT balance FROM accounts WHERE id = 1;      -- reads 0 (dirty read)
TX1: ROLLBACK;                                        -- TX2 acted on data that never existed
```

### Read Committed

Each **statement** sees a fresh snapshot of committed data. Default in PostgreSQL and Oracle.
The `most common approach`!

```sql
TX1: SELECT balance FROM accounts WHERE id = 1;  -- returns 100
TX2: UPDATE accounts SET balance = 80 WHERE id = 1; COMMIT;
TX1: SELECT balance FROM accounts WHERE id = 1;  -- returns 80 (non-repeatable read)
```

### Repeatable Read

The **transaction** gets a snapshot at the start — any row you read stays the same. Default in MySQL/InnoDB.

```sql
TX1: SELECT balance FROM accounts WHERE id = 1;  -- returns 100
TX2: UPDATE accounts SET balance = 80 WHERE id = 1; COMMIT;
TX1: SELECT balance FROM accounts WHERE id = 1;  -- still returns 100 (snapshot)
```

But new rows can still appear (phantom reads):

```sql
TX1: SELECT * FROM accounts WHERE branch = 'A';   -- returns 3 rows
TX2: INSERT INTO accounts (branch, balance) VALUES ('A', 50); COMMIT;
TX1: SELECT * FROM accounts WHERE branch = 'A';   -- returns 4 rows (phantom)
```

### Serializable

Full isolation — the result is the same as if transactions ran one after another. Safest, slowest.

The database either acquires **range locks** (locking-based) or **detects dependency cycles and aborts** one transaction at commit time (MVCC).

Higher isolation = more locking/conflict detection = less throughput.

## How it's implemented

- **Locking-based** (e.g. SQL Server) — the database holds read/write locks for longer at higher levels
- **MVCC** (e.g. PostgreSQL, MySQL) — each transaction sees a snapshot of the data (essentially optimistic locking at the engine level); still needs conflict detection at Serializable

In practice, most applications use **Read Committed** + explicit `SELECT ... FOR UPDATE` on the rows that need protection, rather than raising the entire isolation level

The standard defines levels by which *anomalies* they permit, not by *implementation* — so two engines can both claim "repeatable read" and still behave differently. PostgreSQL's repeatable read, for instance, is snapshot isolation and blocks phantoms too, which the standard doesn't require.

## Deadlocks

- Two transactions each hold a lock the other wants. The engine detects the cycle and **kills one** with an error
- Mitigation: acquire locks in a consistent order, keep transactions short, and retry the victim
- Application code that runs transactions **must be prepared to retry** — at Serializable this is not optional, since the engine aborts transactions as a normal part of operation

## Practical notes

- Keep transactions short — a long one holds locks, pins old row versions (blocking MVCC cleanup — see above), and blocks [WAL](../wal.md) recycling
- Never leave a transaction open across a network call or user think-time
- Defaults differ per engine (PostgreSQL read committed, MySQL/InnoDB repeatable read, SQLite serializable) — a classic source of portability bugs
