# Isolation

Concurrent transactions are isolated from one another — each behaves as if it were the only transaction running.

## Read Anomalies

Isolation levels exist to prevent these problems:

- **Dirty read** — reading data that another transaction hasn't committed yet (it might roll back)
- **Non-repeatable read** — reading the same row twice in one transaction and getting different values because another transaction committed in between
- **Phantom read** — running the same query twice and getting new rows because another transaction inserted them in between

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

In practice, most applications use **Read Committed** + explicit `SELECT ... FOR UPDATE` on the rows that need protection, rather than raising the entire isolation level — see `distributed-systems/concurrency/locking.md`.
