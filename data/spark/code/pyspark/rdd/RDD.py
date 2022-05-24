from pyspark import SparkContext

sc = SparkContext()
rdd = sc.parallelize([1, 2, 3, 4])

# RDD Transformations (returns a new RDD)
rddTransformed = rdd.filter(lambda item: 'lol' in item)
rddTransformed = rdd.map(lambda item: item * item)
rddTransformed = rdd.reduceByKey(lambda key, val: "{key}:{val}")  # foreach key
rddTransformed = rdd.mapValues(lambda val: val)
rddTransformed = rdd.sortBy(lambda col: col[0])  # sort by the 1st column (asc)

# RDD Actions
result = rdd.count()  # count of results
result = rdd.first()  # first result
result = rdd.collect()  # all results
result = rdd.take(10)  # 10 random results
result = rdd.top(10)  # first 10 results
