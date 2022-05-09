# MySQL

## Login

```shell
# Simple login
mysql -u "user" -p"pass"
mysql -u root -p123

# Login and choose database
mysql -u "user" -p"pass" "db"
mysql -u root -p123 mydb

## Login to a remote host
mysql -u root -h "remote-ip" -p
```

## Warnings

`SHOW WARNINGS;`

- Warnings can be displayed after a "Query OK, 1 row afected, 1 warning"
- Common warnings:
  - Wrong data value inserted
  - No value into a NOT NULL field

## Source file

```shell
mysql -u root -p123 < script.sql
```

```sql
SOURCE script.sql
```

```sql
LOAD DATA LOCAL INFILE 'ml-100k/u.item' INTO TABLE movielens.movies CHARACTER SET latin1
FIELDS TERMINATED BY '|' (movieID, title, @var3)
SET releaseDate = STR_TO_DATE (@var3, '%d-%M-%Y');
```

## Backup the whole DB

```shell
mysqldump -u `root` -p `db-to-backup` > `path/to/save.sql`
mysqldump -u root -p testdb > /tmp/db.sql
```

## Run an expression

```shell
mysql -uroot -p123 -e "INSERT INTO my-table VALUES (0, 'name', 'lastname', 'age')"
```

## Manage users

```shell
# Create new user
CREATE USER 'new-user'@'localhost' IDENTIFIED BY 'new-password';
GRANT ALL PRIVILEGES ON * . * TO 'new-user'@'localhost';
FLUSH PRIVILEGES;

## Change password security (for newer mysql versions)
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
```

```shell
# Force SSL usage
GRANT USAGE ON *.* TO 'mysqluser'@'%' REQUIRE SSL
```

## Useful SQL commands

```shell
SHOW DATABASES # Show databases
SHOW GLOBAL VARIABLES LIKE 'PORT'; # Check port
SELECT @@hostname; # Check hostname
```
