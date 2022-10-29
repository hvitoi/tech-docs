# Jenkins & MySQL & Ubuntu with connection to AWS

- This app has three systems
  - A `Jenkins server`
  - A `Ubuntu` OS with the `awscli` and a `mysql-client`
  - A `MySQL server`
- The goal is the backup the data from the mysql server to upload it to AWS S3 bucket
- The upload will be scheduled by means of Jenkins

## Credentials

- `jenkins`
  - user: admin
  - password: 123
- `ubuntu`
  - user: ubuntu
  - password: 123
- `mysql`
  - user: root
  - password: 123

## MySQL Server

```sql
CREATE DATABASE testdb;
USE testdb;
CREATE TABLE info (NAME VARCHAR(20), lastname VARCHAR(20), age INT(2));
INSERT INTO info VALUES ('henrique', 'vitoi', 26);
SELECT * FROM info;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';
```

## Test Connections

```sh
# Test connection from jenkins to ubuntu
ssh -i "~/ubuntu.key" "ubuntu@ubuntu"

# Test connection from ubuntu to mysql
mysql -u "root" -h "mysql" -p

# Dump mysql database on ubuntu
mysqldump -u "root" -h "mysql" -p "123" > "/tmp/db.sql" # mysql is the db hostname
```

## Steps in AWS

1. Create a `S3` bucket
1. Add a user at `IAM` and give it full access to S3
1. Download the .csv file with the credentials of the user (`access key id` and `secret access key`)

## Ubuntu

```sh
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
aws s3 cp "/tmp/db.sql" "s3://hvitoi/db.sql" # Copy a sql dump into S3
```

## Jenkins

- 2 secrets: MySQL password and AWS secret

- `Dashboard` / `Manage Jenkins` / `Manage Credentials` / `Add Credential`

  - Add `Secret text`
  - MYSQL_PASSWORD: 123
  - AWS_SECRET_ACCESS_KEY: ...
  - AWS_BUCKET_NAME: hvitoi
  - ...

- `Dashboard` / `New Item`
  - `Build Environment` / `Use secret text or file` / `Secret text`
