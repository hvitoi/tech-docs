-- A transaction groups statements into a single all-or-nothing unit (ACID)
-- If any step fails, the whole transaction is rolled back and the database is left untouched
-- Classic example: transfer 100 from account 1 to account 2 (the money must never exist in both or neither)
-- The isolation level is optional; the standard also allows setting it with a separate SET TRANSACTION
-- statement issued *before* the transaction starts (MySQL requires that form)
-- READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE
START TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Locks the row until the transaction ends, so a concurrent transfer cannot read a stale balance
-- Not core standard SQL: the standard only defines FOR UPDATE on a DECLARE CURSOR
SELECT
  balance
FROM
  account
WHERE
  id = 1 FOR
UPDATE
;

UPDATE
  account
SET
  balance = balance - 100
WHERE
  id = 1;

UPDATE
  account
SET
  balance = balance + 100
WHERE
  id = 2;

-- Intermediate marker: the audit log is nice-to-have, the transfer is not
SAVEPOINT after_transfer;

INSERT INTO
  audit_log (account_id, action, amount)
VALUES
  (1, 'transfer_out', 100);

-- Undo only up to the savepoint (the two UPDATEs survive, the INSERT is discarded)
-- The transaction stays open and can still be committed
ROLLBACK TO SAVEPOINT after_transfer;

-- Discards the savepoint without undoing anything (frees the marker)
RELEASE SAVEPOINT after_transfer;

-- Makes every change since START TRANSACTION durable and visible to other transactions
-- Note: DDL (CREATE/ALTER/DROP) commits implicitly in some engines (MySQL, Oracle), so it cannot be rolled back there
COMMIT;

-- Discards every change since START TRANSACTION (or since the last COMMIT/ROLLBACK)
-- Used in the error path, e.g. when the debited account would end up with a negative balance
ROLLBACK;
