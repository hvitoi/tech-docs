# Locking

- **Pessimistic**
  - assumption conflict is likely → block first, ask questions later
  - acquire a lock before accessing the resource; other threads block
- **Optimistic**
  - conflict is rare → just do the work, verify on commit
  - read state, compute new state, `compare-and-swap (CAS)` (write only if state hasn't changed), retry on failure

## Pessimistic Locking (conservative)

- Acquires an **exclusive lock** on the resource before reading/writing
- Guarantees no concurrent modification, but `introduces contention` (multiple threads waiting for the same lock) and `reduces throughput`

### SQL

```sql
-- all within the same transaction
SELECT balance FROM accounts WHERE id = 42 FOR UPDATE;   -- acquires lock, balance=100
UPDATE accounts SET balance = balance - 20 WHERE id = 42; -- balance=80
COMMIT;                                                   -- releases lock
```

### DynamoDB

- DynamoDB does not support pessimistic locking natively (no `FOR UPDATE` equivalent)

### HTTP

- HTTP is stateless — no standard mechanism to hold a lock between requests

## Optimistic Locking

- Does **not** hold a lock — instead, each write carries a `version` or `timestamp`
- Before writing, check whether the version has changed since the read
- If it changed, the write is rejected and the caller retries or aborts
- Implemented via **conditional writes** (e.g. `UPDATE ... WHERE version = ?`)

### SQL -

```sql
SELECT balance, version FROM accounts WHERE id = 42;  --> balance=100, version=3
UPDATE accounts SET balance = balance - 20, version = 4 WHERE id = 42 AND version = 3;
-- 0 rows affected → someone else changed it, retry from SELECT
```

### DynamoDB -

```json
// 1. GetItem → balance=100, version=3
{
  "TableName": "accounts",
  "Key": {
    "id": { "N": "42" }
  }
}


// 2. Conditional UpdateItem
{
  "TableName": "accounts",
  "Key": {
    "id": { "N": "42" }
  },
  "UpdateExpression": "SET balance = balance - :amt, version = version + :one",
  "ConditionExpression": "version = :v",
  "ExpressionAttributeValues": {
    ":amt": { "N": "20" },
    ":v": { "N": "3" },
    ":one": { "N": "1" }
  }
}

// throws ConditionalCheckFailedException if version changed → retry
```

### HTTP (ETags)

```shell
# 1. GET → returns ETag header
curl -i http://api.example.com/accounts/42
# → 200 OK
# → ETag: "v3"
# → {"balance":100}

# 2. PUT with If-Match → only succeeds if ETag still matches
curl -X PUT http://api.example.com/accounts/42 \
  -H 'If-Match: "v3"' \
  -H 'Content-Type: application/json' \
  -d '{"balance":80}'

# → 200 OK (ETag matched, update applied)
# → 412 Precondition Failed (ETag changed → retry from GET)
```
