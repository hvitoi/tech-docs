-- Return only unique release years
SELECT
  DISTINCT release_year
FROM
  film;

-- Select all the have unique fname+lname combination
SELECT
  DISTINCT author_fname,
  author_lname
FROM
  books;

-- Do not select only if the row is completely equal!
SELECT
  DISTINCT *
FROM
  books;