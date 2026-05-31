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
