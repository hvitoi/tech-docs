# Install MySql

- Download the latest MySQL Community Server

```shell
# Checking MySQL service
systemctl status "mysql"
systemctl start "mysql"
systemctl stop "mysql"

# set environment variables for a service
systemctl set-environment MYSQLD_OPTS="--skip-grant-tables --skip-networking"
```

## Test connection

```sql
SHOW databases;
```

## Source .sql command in MySQL CLI

```shell
source $(pwd)/script.sql
```
