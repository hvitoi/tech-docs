from pyspark.sql import SparkSession
from pyspark.sql import Rows
from pyspark.sql import functions

spark = SparkSession.builder.appName("MyApp").getOrCreate()
rdd = spark.read.text("file.txt").rdd
df = spark.createDataFrame(rdd)

# DataFrame -> GroupedData
myGroup = df.groupBy("movieId")

# GroupedData
myGroup.avg("rating")  # returns DataFrame
myGroup.count()  # returns DataFrame
