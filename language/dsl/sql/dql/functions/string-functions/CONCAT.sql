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
