--
SELECT
  *
FROM
  actor;

--
SELECT
  first_name,
  last_name
FROM
  actor;

--
SELECT
  *
FROM
  bank_account
WHERE
  iban = "FR10474608000002006107XXXXX"
  AND bic = "OIVUSCLQXXX"
FOR UPDATE; -- locks the row for update
