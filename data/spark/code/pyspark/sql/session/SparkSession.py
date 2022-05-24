from pyspark.sql import SparkSession
from pyspark.sql import Rows
from pyspark.sql import functions

# Spark Session (Spark 2.0 way of creating a context)
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# RDD -> DataFrame
rdd = spark.read.text("file.txt").rdd  # alternative to sc.textFile
df = spark.createDataFrame(rdd)

# Stop session
spark.stop()
