from pyspark.sql import SparkSession
from pyspark.sql import Rows
from pyspark.sql import functions

spark = SparkSession.builder.appName("MyApp").getOrCreate()
rdd = spark.read.text("file.txt").rdd
df = spark.createDataFrame(rdd)

# DataFrame
df.cache()  # used when you are going to use a DF often unchanged
df.groupBy("movieId")  # returns a GroupedData object
df.orderBy("avg(rating)")  # order data
df.sort(df.someColumn.desc())  # sort by a column
df.join(otherDataFrame, "movieId")  # joins another DataFrame in a col
df.filter("userID = 0")  # filter only certain values
df.select("movieID")  # get only a column
df.withColumn("dummyCol", lit(0))  # add a new column
df.collect()  # returns an iterable object
