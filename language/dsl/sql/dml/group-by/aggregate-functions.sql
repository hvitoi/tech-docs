--
SELECT
  AVG(amount)
FROM
  payment;

--
SELECT
  ROUND(AVG(amount), 2)
FROM
  payment;

--
SELECT
  MIN(amount)
FROM
  payment;

-- Select only one row. Most expensive payment
SELECT
  MAX(amount)
FROM
  payment;

--
SELECT
  SUM(amount)
FROM
  payment;




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
