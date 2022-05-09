-- Display a column as another name
SELECT
  payment_id AS my_payment
FROM
  payment;

-- AS can be used without AS too!
SELECT
  payment_id my_payment
FROM
  payment;

--
SELECT
  customer_id as cliente,
  SUM(amount) AS total_spent
FROM
  payment
GROUP BY
  customer_id;