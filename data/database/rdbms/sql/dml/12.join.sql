/* CROSS JOIN: Each record in T1 has a row for every record in T2. It's the most basic kind of join */
SELECT
  *
FROM
  customers,
  orders;

-------------------------
/* INNER JOIN: Show only the tables that have a matching ID field and merge them together */
-- Implicit inner join
SELECT
  *
FROM
  customers,
  orders
WHERE
  customers.id = orders.customer_id;

-- Explicit inner join
SELECT
  -- from customers
  first_name,
  last_name,
  -- from orders
  order_date,
  amount
FROM
  customers
  JOIN orders ON customers.id = orders.customer_id;

--
SELECT
  store_id,
  title
FROM
  inventory
  INNER JOIN film ON film.film_id = inventory.film_id
WHERE
  store_id = 1;

SELECT
  film.title,
  count(title) AS copies_at_store1
FROM
  inventory
  INNER JOIN film ON film.film_id = inventory.film_id
WHERE
  store_id = 1
GROUP BY
  title
ORDER BY
  title;

SELECT
  title,
  name AS idioma
FROM
  film
  INNER JOIN language ON language.language_id = film.language_id
WHERE
  name = 'English';

SELECT
  rental.rental_id,
  rental.inventory_id,
  inventory.film_id,
  film.title
FROM
  rental
  INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
  INNER JOIN film ON film.film_id = inventory.film_id;

-- Double INNER JOIN
-------------------------
/* LEFT JOIN: It's an INNER JOIN plus the values from the left table that didn't match with NULL values */
-- Includes customers who haven't made any orders
SELECT
  *
FROM
  customers
  LEFT JOIN orders ON customers.id = orders.customer_id;

-- IFNULL(...) replaces NULL with 0
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
  total_spent DESC;

-------------------------
/* LEFT OUTER JOIN */
-- Retorna todos valores da TabA + valores comuns da TabA e TabB
-- Mostra todos os filmes, inclusive os que estão faltando no inventório
SELECT
  film.film_id,
  inventory_id,
  title
FROM
  film
  LEFT OUTER JOIN inventory ON inventory.film_id = film.film_id;

--Retorna todos valores da TabA exclusivos
SELECT
  film.film_id,
  inventory_id,
  title -- left outer join with where /* 
FROM
  film
  LEFT OUTER JOIN inventory ON inventory.film_id = film.film_id --Mostra somentos os filmes faltando no inventório
WHERE
  inventory_id IS NULL;

--WHERE inventory.film_id IS NULL