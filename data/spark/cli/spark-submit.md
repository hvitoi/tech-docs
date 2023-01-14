# spark-submit

- Submit a python/scala code to be run on the spark cluster
- All the default spark dependencies are already available at this sandbox
- Submit configuration is picked from `SparkConf` file

## Python script

- export `SPARK_MAJOR_VERSION=2` to run with spark 2.0

```shell
spark-submit "script.py"
```

## Scala script

- If scala project, package your `jar` files first
- You jar does not need the spark dependencies given that it is already available in the environment

```shell
spark-submit \
  --master "localhost:4040" \ # mesos://host:port
  --num-executors "2" \
  --executor-memory "1g" \
  --total-executors-cores "" \
  -class "com.me.myproject.Hello" \
  "Hello.jar"
```
