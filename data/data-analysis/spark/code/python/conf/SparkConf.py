from pyspark import SparkContext, SparkConf

# Configuration for the SparkContext
conf = SparkConf().setAppName("myapp")
sc = SparkContext(conf=conf)
