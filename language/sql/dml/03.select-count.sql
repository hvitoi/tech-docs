-- count every row including NULLS
SELECT
  COUNT(*)
FROM
  payment;

-- count only rows in which payment_id is not NULL and match the "where" clause
SELECT
  COUNT(payment_id)
FROM
  payment
WHERE
  amount > 5;

-- returns number of unique values in amount
SELECT
  COUNT(DISTINCT amount)
FROM
  payment;