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
