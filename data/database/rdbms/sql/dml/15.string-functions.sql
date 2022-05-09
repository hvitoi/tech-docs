-- CONCAT
SELECT
  CONCAT(author_fname, ' ', author_lname) as "Author full name"
FROM
  books;

-- CONCAT_WS (concat with symbol)
SELECT
  CONCAT_WS((' - '), author_fname, author_lname, title)
FROM
  books;

-- SUBSTRING (SUBSTR)
-- Take the characters 2 to 5
SELECT
  SUBSTRING(title, 2, 5)
FROM
  books;

-- Take the from 4 on
SELECT
  SUBSTRING(title, 4)
FROM
  books;

-- Take last 2 letters
SELECT
  SUBSTRING(title, -2)
FROM
  books;

-- REPLACE
-- All 'e' will be replaced with '3'
SELECT
  REPLACE (title, 'e', '3')
FROM
  books;

-- REVERSE
SELECT
  REVERSE (title)
FROM
  books;

-- CHAR_LENGTH
-- Length of the field
SELECT
  CHAR_LENGTH(title)
FROM
  books;

-- UPPER
SELECT
  upper(title)
FROM
  books;

-- LOWER
SELECT
  lower(title)
FROM
  books;

-- IFNULL
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

-- NULLIF
-- Takes 2 inputs, return NULL if both are equal, otherwise the first arg is passed
SELECT
  (
    SUM(
      CASE
        THEN department = 'A' THEN 1
        ELSE 0
      END
    ) / NULLIF(
      SUM(
        CASE
          THEN department = 'B' THEN 1
          ELSE 0
        END
      ),
      0
    ) --Prevents a division by 0. Instead divides by NULL
  ) AS department_ratio
FROM
  depts -- COALESCE
  -- Returns the the first argument if it's not null, otherwise returns the second argument
  -- Good for replacing NULL with zeroes 
SELECT
  item,
  (price - COALESCE(discount, 0)) AS final
FROM
  table;

-- CAST
SELECT
  CAST('5' AS INTEGER);

SELECT
  CAST('1980-01-01' AS DATETIME);