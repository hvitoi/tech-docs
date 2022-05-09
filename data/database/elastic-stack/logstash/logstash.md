# Logstash

- Logstash is a process, once it finishes dumping it exits with status code 0

## File log

- Logstash conf file: `txt.conf`
- Data file: `txt-data.txt`

## Mysql

- Logstash conf file: `mysql.conf`
- Setup MySQL database

```shell
docker cp ./Logstash/data/mysql-data:/tmp
docker exec -it mysql bash
mysql -u root -p
```

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123';

CREATE DATABASE movielens;

CREATE TABLE movielens.movies (
  movieID INT PRIMARY KEY NOT NULL,
  title TEXT,
  releaseDate DATE
);

LOAD DATA LOCAL INFILE 'mysql-data/u.item' INTO TABLE movielens.movies CHARACTER SET latin1
FIELDS TERMINATED BY '|' (movieID, title, @var3)
SET releaseDate = STR_TO_DATE (@var3, '%d-%M-%Y');
```

- Download JDBC drivers in Logstash container
  - <https://dev.mysql.com/downloads/connector/j/8.0.html>

```shell
curl -O https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.22.zip
unzip mysql-connector-java-8.0.22
docker cp ./mysql-connector-java-8.0.22 mysql:/tmp
```

## CSV

- Comma Separated Values

- Logstash conf file: `csv.conf`
- Data file: `csv-data.csv`

## JSON

- Logstash conf file: `json.conf`, `json-split.conf`
- Data file: `json-data.json`, `json-data-split.json`

## S3

- Logstash conf file: `s3.conf`
- The data is stored in a s3 bucket containing raw apache logs
