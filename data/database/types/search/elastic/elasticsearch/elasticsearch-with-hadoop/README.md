# Elasticsearch with Hadoop MR

This is the source code for a lesson on using Elasticsearch with Hadoop MR.

## Build jar with

```shell
mvn clean package
```

## Get sample logs

```shell
wget https://raw.githubusercontent.com/linuxacademy/content-elastic-log-samples/master/access.log
cp target/eswithmr-1.0-SNAPSHOT.jar . # copy the jar to the same level of the access log
```

## Execute hadoop

```shell
hadoop jar eswithmr-1.0-SNAPSHOT.jar access.log
```

## Check index

```shell
curl -XGET "localhost:9200/_cat/indicies?v"
```
