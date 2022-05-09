-- For each group, you can apply an aggregate function (AVG, SUM, MAX...)
-- No aggregate function
-- GROUP BY without aggregate function (Same as a SELECT DISTINT customer_id)
SELECT
  customer_id
FROM
  payment
GROUP BY
  customer_id
ORDER BY
  customer_id ASC;

-- COUNT
-- Count the grouped rows (does NOT include null), count(*) would include null
SELECT
  customer_id,
  COUNT(customer_id)
FROM
  payment
GROUP BY
  customer_id
ORDER BY
  customer_id ASC;

-- SUM
-- ORDER BY SUM(amount)
SELECT
  customer_id,
  SUM(amount)
FROM
  payment
GROUP BY
  customer_id
ORDER BY
  SUM DESC;

-- AVG
SELECT
  rating,
  ROUND(AVG(rental_rate), 1)
FROM
  film
GROUP BY
  rating;

-- COUNT and SUM
SELECT
  staff_id,
  COUNT(amount),
  SUM(amount)
FROM
  payment
GROUP BY
  staff_id;

-- MIN 
-- For each author, take the first release year
SELECT
  author_fname,
  author_lname,
  min(released_year)
FROM
  books
GROUP BY
  author_fname,
  author_lname
ORDER BY
  author_fname ASC;

-- Double GROUPBY
-- Counting the GROUPED ROWS (in this case the row firstname+lastname)
SELECT
  author_fname,
  author_lname,
  count(*)
FROM
  books
GROUP BY
  author_fname,
  author_lname;