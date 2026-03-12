SELECT
  RANK() OVER (
    ORDER BY
      salary DESC
  )
FROM
  employees;
