-- This is the standard SQL "if/else"
SELECT
  CASE
    WHEN age < 18 THEN 'minor'
    ELSE 'adult'
  END
FROM
  people;
