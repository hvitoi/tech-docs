# MySQL CLI

## user/pass

```shell
# Simple login
mysql -u "user" -p"pass"
mysql -u root -p123

# Login and choose database
mysql -u "user" -p"pass" "db"
```

```shell
# source a sql script
# alternatively use "SCRIPT script.sql"
mysql -u "root" -p123 < "script.sql"
```

## host

- Login to a remote host

```shell
mysql -u root -h "remote-ip" -p
```

## expression

- Run an expression

```shell
mysql \
  -uroot \
  -p123 \
  -e "INSERT INTO my-table VALUES (0, 'name', 'lastname', 'age')"
```

## mysqldump

- Backup the whole DB

```shell
mysqldump -u "root" -p "db-to-backup" > "path/to/save.sql"
mysqldump -u "root" -p "testdb" > "/tmp/db.sql"
```
