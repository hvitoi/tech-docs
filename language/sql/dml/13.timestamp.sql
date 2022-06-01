/* EXTRACT (timestamp) */
CREATE TABLE person (
  name VARCHAR(100),
  birthdate DATE,
  birthtime TIME,
  birthdt DATETIME
);

INSERT INTO
  person (name, birthdate, birthtime, birthdt)
VALUES
  (
    'Padma',
    '1983-11-11',
    '10:07:35',
    '1983-11-11 10:07:35'
  ),
  (
    'Larry',
    '1943-12-25',
    '04:10:42',
    '1943-12-25 04:10:42'
  );

('Toaster', '2017-04-21') -- Current date-time
SELECT
  CURDATE();

-- CURDATE (today)
SELECT
  CURTIME();

-- CURTIME
SELECT
  NOW();

-- NOW
INSERT INTO
  person (name, birthdate, birthtime, birthdt)
VALUES
  ('Microwave', CURDATE(), CURTIME(), NOW());

-- EXTRACT
SELECT
  EXTRACT(
    MONTH
    from
      payment_date
  ) AS month,
  SUM(amount) AS total
FROM
  payment
GROUP BY
  month
ORDER BY
  total DESC;

-- DATE_FORMAT
-- was born on a Friday
SELECT
  name,
  DATE_FORMAT(birthdt, 'Was born on a %W')
FROM
  person;

-- DATE MATH
-- difference in days
SELECT
  DATEDIFF(NOW(), birthdt);

-- 1 month after now
SELECT
  DATE_ADD(NOW(), INTERVAL 1 MONTH);

-- 1 month before now + 10 hours
SELECT
  NOW() - INTERVAL 1 MONTH + INTERVAL 10 HOUR;

-- CREATED AT & CHANGED AT
CREATE TABLE comments (
  content VARCHAR(100),
  created_at TIMESTAMP DEFAULT NOW(),
  changed_at TIMESTAMP DEFAULT NOW() ON
  UPDATE CURRENT_TIMESTAMP -- or ON UPDATE NOW
);

-- CAST 
SELECT
  name,
  birthdt
FROM
  people
WHERE
  birthdt BETWEEN CAST('1980-01-01' AS DATETIME)
  AND CAST('2000-01-01' AS DATETIME);