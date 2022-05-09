-- WHERE is applied before the GROUP BY, HAVING is applied after the GROUP BY
-- Este HAVING é adequado, pois usa uma aggregate function para filtragem
SELECT
  customer_id,
  sum(amount)
FROM
  payment
GROUP BY
  customer_id
HAVING
  SUM(amount) > 200;

--
SELECT
  store_id,
  COUNT(customer_id)
FROM
  customer
GROUP BY
  store_id
HAVING
  store_id = 1;

--
SELECT
  rating,
  AVG(rental_rate)
FROM
  film
WHERE
  rating IN ('R', 'G', 'PG')
GROUP BY
  rating;

-- Este HAVING não é adequado, pois poderia ser filtrado com WHERE antes
SELECT
  rating,
  AVG(rental_rate)
FROM
  film
GROUP BY
  rating
HAVING
  rating IN ('R', 'G', 'PG');

--
SELECT
  customer_id,
  count(customer_id)
FROM
  payment
GROUP BY
  customer_id
HAVING
  count(customer_id) >= 40
ORDER BY
  count(customer_id) DESC;