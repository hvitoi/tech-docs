-- Limit number of rows returned
SELECT
  *
FROM
  customer
LIMIT
  5;

-- MYSQL SYNTAX (for a similar behavior in PostgreSQL/SQLite use OFFSET)
SELECT
  title
FROM
  books
LIMIT
  10, 20; -- rows 11 through 30 (same as LIMIT 20 OFFSET 10)
