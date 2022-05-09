# Install MySql

- Download the latest MySQL Community Server via MySQL APT

```shell
dpkg -i mysql.deb # Select MySQL Server & Cluster / mysql-8.0
sudo apt update
sudo apt install mysql-server

## Checking MySQL service
systemctl status mysql
systemctl start mysql
systemctl stop mysql
```

## Test connection

```sql
SHOW databases;
```

## Source .sql command in MySQL CLI

```bash
source $(pwd)/script.sql
```

## Docker

```shell
## Pull, Build and Run
docker pull mysql
docker build -t hvitoi/mysql . # Only if creating a new image from Dockerfile
docker run --name meusql -d -v /home/hvitoi/dados/mysql:/var/lib/mysql -p 3305:3306 -e MYSQL_ROOT_PASSWORD=123 mysql

## Exec
docker exec -it meusql /bin/bash
docker exec -it meusql mysql -uroot -p123
```
