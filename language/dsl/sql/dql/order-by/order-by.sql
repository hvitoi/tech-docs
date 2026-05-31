--
SELECT
  first_name,
  last_name
FROM
  customer
ORDER BY
  first_name ASC;

--
SELECT
  first_name,
  last_name
FROM
  customer
ORDER BY
  first_name DESC;

--
SELECT
  first_name,
  last_name
FROM
  customer
WHERE
  first_name = 'Kelly'
ORDER BY
  first_name ASC,
  last_name ASC;

--
SELECT
  first_name
FROM
  customer
ORDER BY
  last_name;

-- order by author_fname DESC, and then author_lname ASC
SELECT
  title,
  author_fname,
  author_lname
FROM
  books
ORDER BY
  2 DESC,
  3;