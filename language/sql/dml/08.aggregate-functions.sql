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

--
SELECT
  COUNT(amount)
FROM
  payment;