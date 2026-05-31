-- where is case INSENSITIVE by default
SELECT
  *
FROM
  customer
WHERE
  first_name = 'Jamie'
  AND last_name = 'Rice';

--
SELECT
  *
FROM
  payment
WHERE
  amount = 4.99
  OR amount != 7.99;

-- compare column1 with column2
SELECT
  *
FROM
  client
WHERE
  first_name = last_name;