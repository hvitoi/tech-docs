-- Returns the first non-NULL value
-- Good for replacing NULL with zeroes (or any other default value)
SELECT
  COALESCE(email, "me@example.com")
FROM
  users;
