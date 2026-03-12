-- Returns NULL if two expressions are equal
SELECT
  NULLIF(10, 10);

-- Often used to avoid division by zero:
SELECT
  value / NULLIF(count, 0)
