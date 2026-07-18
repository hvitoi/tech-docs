# SQLite

- Embedded and portable relational database: a C library linked into the app, not a client/server DBMS
- The whole database is a `single file` (`.db`/`.sqlite`)
- No daemon, no port, no user accounts, no GRANT
- Access control is just filesystem permissions on that file
- <https://sqlite.org>

## When to use

- ✅ App-local storage, on-disk cache, tests, CLI tools, analytics on a file, edge/embedded, read-heavy websites
- ❌ Many concurrent writers, network access from multiple machines, DB-level user permissions, huge datasets (>~TB)

## Architecture

- `Pager` — reads/writes fixed-size pages (default 4096 B), manages cache + transactions
- `B-tree` — every table and index is a B-tree; the table B-tree is keyed by `rowid`
- `VDBE` — SQL is compiled into bytecode for a virtual machine (see `EXPLAIN`)
- Everything (schema, tables, indexes) lives in the one file; `sqlite_master` is the schema table

## Types (dynamic typing)

- SQLite has **storage classes**, not strict column types: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`
- Types are on the **value**, not the column. A declared `INTEGER` column happily stores `'hello'`
- The declared type only sets a `type affinity` (a conversion preference)
- No native `BOOLEAN` (use `0`/`1`) and no native `DATE` (use TEXT ISO-8601, INTEGER epoch, or REAL julian day)
- Since 3.37: `CREATE TABLE ... STRICT` enforces real types

```sql
CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT NOT NULL) STRICT;
```

- Type affinity
  1. Contains "INT" → `INTEGER` affinity
  2. Contains "CHAR", "CLOB", or "TEXT" → `TEXT`
  3. Contains "BLOB" or is empty → `BLOB` (no affinity)
  4. Contains "REAL", "FLOA", or "DOUB" → `REAL`
  5. Otherwise → `NUMERIC`

## rowid

- Every table has a hidden 64-bit `rowid` primary key unless declared `WITHOUT ROWID`
- `INTEGER PRIMARY KEY` (exactly that spelling) **aliases** the rowid — no second B-tree, fastest lookup
- `INT PRIMARY KEY` or `TEXT PRIMARY KEY` does *not* alias it

## Concurrency

- Locking is at the **whole-database** level, not row or table
- No MVCC — the whole-file lock is the isolation mechanism
- Default `rollback journal`: one writer, and writers block readers
- `WAL mode`: readers never block the writer and vice-versa — **one writer at a time still**
- `SQLITE_BUSY` is the error you get when the write lock isn't free; set a busy timeout

```sql
PRAGMA journal_mode = WAL;      -- persists in the file, set once
PRAGMA busy_timeout = 5000;     -- ms, per-connection
PRAGMA foreign_keys = ON;       -- OFF by default!, per-connection
PRAGMA synchronous = NORMAL;    -- safe with WAL, much faster than FULL
```

- WAL adds two sidecar files: `mydb.db-wal` and `mydb.db-shm`
- WAL requires shared memory → **does not work over NFS or network filesystems**

## Transactions

- ACID, and always `serializable` — the strictest level, for free, because there is only ever one writer
- `BEGIN` is *deferred* by default: the write lock is only taken at the first write, so a read-then-write txn can fail with `SQLITE_BUSY`. Use `BEGIN IMMEDIATE` when you know you'll write

## Notable features

- `Full-text search` via the `FTS5` virtual table
- `JSON` functions (`json_extract`, `->`, `->>`) built in since 3.38
- Window functions, CTEs, `UPSERT` (`ON CONFLICT DO UPDATE`), generated columns
- `:memory:` databases for tests
- Backup API / `VACUUM INTO 'file.db'` for a consistent hot copy — never `cp` a live DB

## GUI

```shell
# DBeaver
brew install dbeaver-community --cask

# DB Browser for SQLite
brew install db-browser-for-sqlite --cask
```
