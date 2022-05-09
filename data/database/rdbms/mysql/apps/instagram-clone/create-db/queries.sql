-- User who joined earlier
SELECT name, email, created_at
FROM user
WHERE created_at = (
SELECT min(created_at)
FROM user
);

-- Count by month joined
SELECT DATE_FORMAT(created_at, '%M') AS month, COUNT(*) AS total
FROM user
GROUP BY month
ORDER BY total DESC;

-- Users with yahoo email
SELECT COUNT(email)
FROM user
WHERE email LIKE '%@yahoo.com';

-- Count by email provider
SELECT
  CASE
    WHEN email LIKE '%@gmail.com' THEN 'gmail'
    WHEN email LIKE '%@yahoo.com' THEN 'yahoo'
    WHEN email LIKE '%@hotmail.com' THEN 'hotmail'
    ELSE 'other'
  END AS provider,
  COUNT(*) AS total_users
FROM user
GROUP BY provider
ORDER BY total_users DESC;