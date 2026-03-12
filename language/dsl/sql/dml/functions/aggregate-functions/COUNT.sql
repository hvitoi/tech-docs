-- count every row including NULLS
SELECT
  COUNT(*)
FROM
  payment;

-- count only rows in which the field is not NULL
SELECT
  COUNT(amount)
FROM
  payment;

-- returns number of unique values in amount
SELECT
  COUNT(DISTINCT amount)
FROM
  payment;
