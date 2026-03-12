SELECT
  ROW_NUMBER() OVER (
    ORDER BY
      salary
  )
FROM
  employees;
