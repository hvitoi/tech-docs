-- if any of the steps in the transaction fails, the transaction whole fails
-- A transaction, by definition, must be atomic, consistent, isolated, and durable (ACID)
-- Applies to DML commands such as INSERT, UPDATE, and DELETE.

BEGIN TRANSACTION transaction_name ;
SET TRANSACTION [ READ WRITE | READ ONLY ]; -- optional, (e.g., transaction isolation level, access modes, etc)

DELETE FROM Student WHERE AGE = 20;

COMMIT; -- saves all the transactions to the database since the last COMMIT or ROLLBACK
ROLLBACK; -- undo transactions since the last COMMIT or ROLLBACK command was issued.
