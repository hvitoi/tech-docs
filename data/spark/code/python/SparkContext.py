from pyspark import SparkContext, SparkConf

# Spark Context: Spark cluster connection
conf = SparkConf().setAppName("myapp")
sc = SparkContext(conf=conf)

# Create RDD
rdd = sc.textFile('hdfs://home/numbers.txt')  # from text file
rdd = sc.parallelize([1, 2, 3, 4])  # from memory

# RDD Transformations (returns a new RDD)
rddTransformed = foo.filter(lambda item: 'lol' in item)
rddTransformed = foo.map(lambda item: item * item)
rddTransformed = foo.reduceByKey(lambda key, val: "{key}:{val}")  # foreach key
rddTransformed = foo.mapValues(lambda val: val)
rddTransformed = foo.sortBy(lambda col: col[0])  # sort by the 1st column (asc)


# RDD Actions
result = foo.count()  # count of results
result = foo.first()  # first result
result = foo.collect()  # all results
result = foo.take(10)  # 10 random results
