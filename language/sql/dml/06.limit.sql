-- Limit number of rows returned
SELECT
  *
FROM
  customer
LIMIT
  5;

-- Take 5 results starting from the 2nd
SELECT
  title
FROM
  books
LIMIT
  2, 5;

-- Take all starting from the 4th
SELECT
  title
FROM
  books
LIMIT
  4, 18446744073709551615;