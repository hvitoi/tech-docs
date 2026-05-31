-- Combine rows with other rows in the same table
SELECT
  a.customer_id,
  a.first_name,
  a.last_name,
  b.customer_id,
  b.first_name,
  b.last_name
FROM
  customer AS a,
  customer AS b
WHERE
  a.first_name = b.last_name;

--
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name IN (
    SELECT
      last_name
    FROM
      customer
  );

--
SELECT
  a.customer_id,
  a.first_name,
  a.last_name,
  b.customer_id,
  b.first_name,
  b.last_name
FROM
  customer AS a
  JOIN customer AS b ON a.first_name = b.last_name;