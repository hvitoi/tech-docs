# Atomicity

- A transaction is `all or nothing` — if any step fails, the entire transaction is rolled back and the database is left unchanged
- Implemented via **undo logs** (also called rollback logs): the database records the inverse of each operation so it can reverse partial changes on failure

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 20 WHERE id = 1;
  UPDATE accounts SET balance = balance + 20 WHERE id = 2;
COMMIT; -- both succeed, or neither does
```
