from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession
from pyspark.sql import Rows
from pyspark.sql import functions

spark = SparkSession.builder.appName("MyApp").getOrCreate()
rdd = spark.read.text("file.txt").rdd
df = spark.createDataFrame(rdd)

# ALS (Alternating Least Squares)
# this is a Machine Learning recommendation algorithm
estimator = ALS(maxIter=5,
                regParam=0.01,
                userCol="userID",
                itemCol="movieID",
                ratingCol="rating")

# trains a model with a dataframe
model = estimator.fit(df)

# run recommendation model for a set of movies that you'd like to recommend
recommendations = model.transform(recommendedMoviesDf)

# get top 20 recommendations
topRecommendations = recommendations.sort(
    recommendations.prediction.desc()).take(20)
