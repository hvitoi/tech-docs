-- Replaces NULL with 0
SELECT
  first_name,
  last_name,
  IFNULL(SUM(amount), 0) AS total_spent
FROM
  customers
  LEFT JOIN orders ON customers.id = orders.customer_id
GROUP BY
  customers.id
ORDER BY
  total_spent;
