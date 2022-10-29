# Scoop CLI

## import

- Import job
- Import a table from a relational database
  - Into HDFS: by default to `/user/username/tablename`
  - Into Hive (on HDFS): by default to `/apps/hive/warehouse/tablename`

```sh
sqoop import \
  --connect "jdbc:mysql://localhost/movielens" \
  --driver "com.mysql.jdbc.Driver" \
  --table "movies" \
  --num-mappers "1" \ `# how many MapReduce mappers to execute the job`
  --hive-import `# import straight into hive`
```

## export

- Export job
- Export table from HDFS (a file) to a relational database

```sh
sqoop export \
  --connect "jdbc:mysql://localhost/movielens" \
  --driver "com.mysql.jdbc.Driver" \
  --table "exported_movies" \ `# table must already exist in MySQL`
  --num-mappers "1" \
  --export-dir "/apps/hive/warehouse/movies" \ `# table to be exported (in Hive)`
  --input-fields-terminated-by '\001' `# what row delimiter is being used in hive table`
  --username "root" `# mysql username`
  --password "123" `# mysql pass`
```
