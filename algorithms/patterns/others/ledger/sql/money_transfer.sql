-- Shared schema for the transfer examples (see optimistic_locking.sql, pessimistick_loging.sql)
-- The CHECK is the ledger invariant: no account may ever go negative
CREATE TABLE accounts (
    account_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    balance DECIMAL(18, 2) NOT NULL CHECK (balance >= 0),
    version INTEGER NOT NULL DEFAULT 0
);

-- SERIALIZABLE stops two concurrent transfers from both reading a balance that only covers one of them
START TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- No procedural guard is needed to check for funds: the CHECK constraint rejects an overdraft,
-- the statement fails, and the client issues the ROLLBACK below instead of the COMMIT
-- Portable alternative without a constraint: add AND balance >= 100 here and inspect the row count
UPDATE
    accounts
SET
    balance = balance - 100
WHERE
    account_id = 1;

UPDATE
    accounts
SET
    balance = balance + 100
WHERE
    account_id = 2;

COMMIT;

-- Error path: on a CHECK violation or a serialization failure, the client discards the whole transfer
ROLLBACK;
