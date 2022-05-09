/* EQUAL */
SELECT
  title
FROM
  books
WHERE
  released_year = 2017;

/* DIFFERENT */
SELECT
  title
FROM
  books
WHERE
  released_year != 2017;

/* GREATER */
SELECT
  title,
  stock_quantity
FROM
  books
WHERE
  stock_quantity >= 100;

--false (0)
SELECT
  'a' > 'b';

--true (1)
SELECT
  'b' > 'a';

--FALSE! They are equal. sql is case insensitive
SELECT
  'A' > 'a';

/* SMALLER */
SELECT
  title,
  released_year
FROM
  books
WHERE
  released_year <= 2000;

-- TRUE! They are equal!
SELECT
  'Q' <= 'q';

/* REST */
-- Only even numbers
SELECT
  title,
  released_year
FROM
  books
WHERE
  released_year % 2 = 0;

/* IS NULL */
SELECT
  title,
  rating
FROM
  series
  LEFT JOIN reviews ON reviews.series_id = series.id
WHERE
  reviews.id IS NULL;

/* AND */
-- && is DEPRECATED!
SELECT
  *
FROM
  books
WHERE
  author_lname = 'Eggers'
  AND released_year > 2010
  AND title LIKE '%novel%';

/* OR */
SELECT
  title,
  author_lname,
  released_year,
  stock_quantity
FROM
  books
WHERE
  author_lname = 'Eggers'
  OR released_year > 2010
  OR stock_quantity > 100;

/* LIKE - ILIKE */
-- % means any sequence or caracters
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE 'Jen%';

-- _ means any single caracter
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE '_her%';

-- \% means the % character. Any name that has % in it.
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE '%\%%';

-- has 4 characters
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name LIKE '____';

-- it's a telephone number
SELECT
  num
FROM
  phone
WHERE
  num LIKE '(__)_____-____';

-- The only difference is that ILIKE is case insensitive
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name ILIKE 'JeN%';

-- NOT LIKE
SELECT
  title
FROM
  books
WHERE
  title NOT LIKE 'W%';

/* BETWEEN */
--equivalent to WHERE (x >= low) AND (x <= high)
SELECT
  title,
  released_year
FROM
  books
WHERE
  released_year BETWEEN 2004
  AND 2015;

--
SELECT
  title,
  released_year
FROM
  books
WHERE
  released_year NOT BETWEEN 2004
  AND 2015;

-- correct using of between with DATETIME!
SELECT
  CAST('2017-05-02' AS DATETIME);

-- Not good! Use CAST!
SELECT
  name,
  birthdt
FROM
  person
WHERE
  birthdt BETWEEN '1980-01-01'
  AND '2000-01-01';

-- BETTER!
SELECT
  name,
  birthdt
FROM
  people
WHERE
  birthdt BETWEEN CAST('1980-01-01' AS DATETIME)
  AND CAST('2000-01-01' AS DATETIME);

/* IN */
--Equivalent to WHERE (x=1) OR (x=2) OR (x=3)...
SELECT
  customer_id,
  rental_id,
  return_date
FROM
  rental
WHERE
  customer_id IN (1, 2, 7)
ORDER BY
  return_date DESC;

-- NOT IN
SELECT
  customer_id,
  rental_id,
  return_date
FROM
  rental
WHERE
  customer_id NOT IN (1, 2)
ORDER BY
  return_date DESC;

/* CASE */
SELECT
  title,
  released_year,
  CASE
    WHEN released_year >= 2000 THEN 'Modern Lit'
    ELSE '20th Century Lit' -- Else here is the 'default'
  END AS genre -- AS CASE-END creates a new column with the alias 'name'
FROM
  books;

--
SELECT
  title,
  stock_quantity,
  CASE
    WHEN stock_quantity BETWEEN 0
    AND 50 THEN '*' -- Multiple if statements
    WHEN stock_quantity BETWEEN 51
    AND 100 THEN '**'
    ELSE '***'
  END AS stock
FROM
  books;

--
SELECT
  title,
  stock_quantity,
  CASE
    WHEN stock_quantity <= 50 THEN '*' -- if statements are executed in the order!
    WHEN stock_quantity <= 100 THEN '**' -- offers the same output as the last
    ELSE '***'
  END AS STOCK
FROM
  books;

--
SELECT
  author_fname,
  author_lname,
  CASE
    WHEN COUNT(*) = 1 THEN '1 book'
    ELSE CONCAT(COUNT(*), ' books')
  END AS COUNT
FROM
  books
GROUP BY
  author_lname,
  author_fname;

SELECT
  CASE
    WHEN email LIKE '%@gmail.com' THEN 'gmail'
    WHEN email LIKE '%@yahoo.com' THEN 'yahoo'
    WHEN email LIKE '%@hotmail.com' THEN 'hotmail'
    ELSE 'other'
  END AS provider,
  COUNT(*) AS total_users
FROM
  user
GROUP BY
  provider
ORDER BY
  total_users DESC;

/* CASE EXPRESSION */
-- similar to switch
SELECT
  num CASE
    num
    WHEN 1 THEN 'one'
    WHEN 2 THEN 'two'
    WHEN 3 THEN 'three'
    ELSE 'other'
  END AS the_number
FROM
  test;

-- case expressions to count things
SELECT
  SUM (
    CASE
      rental_rate
      WHEN 0.99 THEN 1
      ELSE 0
    END
  ) AS bargains,
  SUM (
    CASE
      rental_rate
      WHEN 2.99 then 1
      ELSE 0
    END
  ) AS regular,
  SUM (
    CASE
      rental_rate
      WHEN 4.99 then 1
      else 0
    END
  ) AS premium
FROM
  film;