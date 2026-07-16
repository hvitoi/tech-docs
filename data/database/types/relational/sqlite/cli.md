# SQLite CLI

- The `sqlite3` binary is a standalone shell, already installed on macOS/most Linux

```shell
sqlite3 mydb.db            # open (creates the file lazily on first write)
sqlite3 :memory:           # scratch in-memory db
sqlite3 mydb.db "SELECT 1" # one-shot query
```

## Dot commands

```shell
.help
.tables                 # list tables
.schema users           # DDL of a table
.databases              # attached dbs + file paths
.indexes users
.headers on
.mode box               # box | table | csv | json | markdown | line
.read script.sql        # run a file
.dump > backup.sql      # logical dump (SQL text)
.import data.csv users  # csv -> table
.output out.txt         # redirect results to a file
.quit
```

## Backup / restore

```shell
sqlite3 mydb.db ".backup 'copy.db'"     # consistent hot copy
sqlite3 mydb.db "VACUUM INTO 'copy.db'" # same, also compacts
sqlite3 mydb.db .dump > dump.sql        # text dump
sqlite3 new.db < dump.sql               # restore
```

## Inspect

```shell
sqlite3 mydb.db "PRAGMA integrity_check;"
sqlite3 mydb.db "PRAGMA table_info(users);"
sqlite3 mydb.db "EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = 'a@b.c';"
```

- `EXPLAIN QUERY PLAN` output shows `SCAN` (bad, full table) vs `SEARCH ... USING INDEX` (good)
