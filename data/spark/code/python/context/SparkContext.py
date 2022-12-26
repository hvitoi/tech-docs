from pyspark import SparkContext

# Spark Context: Spark cluster connection
sc = SparkContext()

# Create RDD
rdd = sc.textFile('hdfs://home/numbers.txt')  # from text file
rdd = sc.parallelize([1, 2, 3, 4])  # from memory
