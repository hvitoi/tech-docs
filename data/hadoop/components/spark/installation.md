# Spark installation

## Spark server

- <http://spark.apache.org/>
- Lastest version: 3.0.1

```sh
curl -O "https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz"
```

## Spark client for elasticsearch

- The spark client must match the spark server version and the scala version

```xml
<!-- https://mvnrepository.com/artifact/org.elasticsearch/elasticsearch-spark-20 -->
<dependency>
    <groupId>org.elasticsearch</groupId>
    <artifactId>elasticsearch-spark-20_2.11</artifactId>
    <version>7.10.1</version>
</dependency>
```

## Spark shell

```sh
./spark-2.3.3-bin-hadoop2.7/bin/spark-shell --packages org.elasticsearch:elasticsearch-spark-20 _2.11:7.0.1
```

```scala
import org.elasticsearch.spark.sql._
case class Person(ID:Int, name:String, age:Int, numFriends:Int)
def mapper(line:String): Person = {
  val fields = line.split(',')
  val person:Person = Person(fields(0).toInt, fields(1), fields(2).toInt, fields(3).toInt)
  return person
}

import spark.implicits._
val lines = spark.sparkContext.textFile("fakefriends.csv")
val people = lines.map(mapper).toDF()
people.saveToEs("spark-friends")

:quit
```
