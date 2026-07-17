# https://docs.python.org/3/library/sqlite3.html
# # python -m sqlite3 mydb.db "SELECT * FROM book"

import sqlite3


# autocommit legacy behaviour: the module implicitly opens a transaction before DML and commits before DDL. Use `with con:` blocks, or Python 3.12+ `sqlite3.connect(..., autocommit=False)` for PEP 249 semantics
# Threads: a connection is not sharable across threads by default (`check_same_thread=True`). Give each thread its own connection
# datetime adapters are deprecated since 3.12 — store ISO strings (`dt.isoformat()`) yourself


# Config
con = sqlite3.connect(":memory:")  # or "mydb.db" to open a file
con.row_factory = sqlite3.Row  # rows as dict-like instead of tuples
con.execute("PRAGMA journal_mode = WAL")
# sqlite3.sqlite_version          # the underlying C library version
# con.set_trace_callback(print)   # log every statement executed
# con.backup(sqlite3.connect("copy.db"))  # online backup API


# foreign_keys is OFF by default: and is per-connection — FKs are silently ignored otherwise
con.execute("PRAGMA foreign_keys = ON")

# DDL
con.executescript("""
    CREATE TABLE IF NOT EXISTS author (
        id   INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    ) STRICT;

    CREATE TABLE IF NOT EXISTS book (
        id        INTEGER PRIMARY KEY,
        title     TEXT NOT NULL,
        year      INTEGER,
        author_id INTEGER NOT NULL REFERENCES author(id) ON DELETE CASCADE
    ) STRICT;
""")


# DML
# Starts a transaction, commits on success, rolls back on exception
with con:
    # Use `?`` placeholders, NEVER f-strings (SQL injection)
    # Placeholders like `?` (qmark) or `:name` (named) bind values, never table/column names

    # Runs one SQL statement once
    cursor = con.execute("INSERT INTO author (name) VALUES (?)", ("Borges",))
    author_id = cursor.lastrowid

    # Runs one SQL statement multiple times for each value
    con.executemany(
        "INSERT INTO book (title, year, author_id) VALUES (?, ?, ?)",
        [("Ficciones", 1944, author_id), ("El Aleph", 1949, author_id)],
    )

# DQL
rows = con.execute("SELECT * FROM book WHERE year = :y", {"y": 1944})
rows = con.execute(
    "SELECT b.title, b.year, a.name "
    "FROM book b "
    "JOIN author a "
    "ON a.id = b.author_id "
    "WHERE b.year > ? "
    "ORDER BY b.year",
    (1900,),
)
for row in rows:
    print(row["year"], row["title"], "-", row["name"])

con.close()
