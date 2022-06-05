# MySQL dialect

## USE

```sql
USE mydb;
```

## DESCRIBE

```sql
DESCRIBE mytable;
```

## SHOW

- **WARNINGS**

- Warnings can be displayed after a "Query OK, 1 row afected, 1 warning"
- Common warnings:
  - Wrong data value inserted
  - No value into a NOT NULL field

```sql
SHOW WARNINGS;
```

- **Global**

```sql
SHOW DATABASES -- Show databases
SHOW GLOBAL VARIABLES LIKE 'PORT'; -- Check port
SELECT @@hostname; -- Check hostname
```

## SET

```sql
SET NAMES 'utf8';
SET CHARACTER SET utf8;
```

## SOURCE

```sql
SOURCE script.sql
```

## LOAD DATA

```sql
LOAD DATA
  LOCAL INFILE 'ml-100k/u.item'
  INTO TABLE movielens.movies
CHARACTER
  SET latin1 FIELDS TERMINATED BY '|' (movieID, title, @var3)
  SET releaseDate = STR_TO_DATE (@var3, '%d-%M-%Y');
```

## USER

```sql
-- Create new user
CREATE USER 'new-user'@'localhost'
  IDENTIFIED BY 'new-password';

-- Grant priviledges for that user
GRANT ALL PRIVILEGES
  ON * . *
  TO 'new-user'@'localhost';

-- Apply
FLUSH PRIVILEGES;
```

```sql
-- Change password security (for newer mysql versions)
ALTER USER 'root'@'localhost'
  IDENTIFIED WITH mysql_native_password BY '123';
```

## GRANT

```sql
-- Force SSL usage
GRANT USAGE ON *.* TO 'mysqluser'@'%' REQUIRE SSL
```

```sql
-- Grant priviledges for a user
GRANT ALL PRIVILEGES
  ON mydb.*
  TO user@localhost IDENTIFIED BY 'current-password';
```
