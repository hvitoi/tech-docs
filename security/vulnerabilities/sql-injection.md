# SQL Injection (SQLi)

- Attacker injects SQL into inputs concatenated into a query
- Goal: read data, bypass auth, modify/drop data

```python
# Vulnerable
query = f"SELECT * FROM users WHERE email = '{email}'"
# Input: admin@x.com' --  → password check commented out
```

## Kinds

- `In-band` — result in the HTTP response (`UNION SELECT`)
- `Blind` — no output; infer via
  - `Boolean`: page differs on `AND 1=1` vs `AND 1=2`
  - `Time`: `SLEEP(5)` delays response when true
- `Out-of-band` — exfiltrate via DNS/HTTP
- `Second-order` — input stored, triggers later in a different query

## Prevention

1. **Parameterized queries** — the only reliable fix

    ```python
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    ```

1. **ORMs** (SQLAlchemy, Django, Prisma) — parameterized by default; still vulnerable on `raw()` / `text()` with concatenation
1. **Allowlist identifiers** — column/table names can't be parameterized
1. **Least privilege** DB user — no `DROP`, no `SUPERUSER`
1. **WAF** — defense in depth only; bypassable

## Don't rely on

- Escaping — easy to get wrong
- Input validation — `a'--@x.com` is a valid email string
- Hiding error messages — blind SQLi still works
