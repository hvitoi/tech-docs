-- was born on a Friday
SELECT
  name,
  DATE_FORMAT(birthdt, 'Was born on a %W')
FROM
  person;
