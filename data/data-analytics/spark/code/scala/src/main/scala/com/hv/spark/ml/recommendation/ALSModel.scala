package com.hv.spark.ALSModel

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext
import org.apache.spark.broadcast.Broadcast
import org.apache.spark.ml.recommendation.ALS
import org.apache.spark.ml.recommendation.ALSModel
import org.apache.spark.rdd.RDD
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Dataset
import org.apache.spark.sql.SparkSession
import org.apache.spark.util.LongAccumulator

// Alternating Least Squares

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val model = Init.run()

    // Instance Methods
    ALSModelRecommendForUserSubset.run(model)

  }
}

object Init {
  def run() = {
    val ss: SparkSession = SparkSession
      .builder()
      .appName("MyApp")
      .master("local[*]")
      .getOrCreate()

    import ss.implicits._

    val df: DataFrame = ss.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("ml-latest-small/movies.csv")

    val als: ALS = new ALS()
      .setMaxIter(5)
      .setRegParam(0.01)
      .setUserCol("userID")
      .setItemCol("movieId")
      .setRatingCol("rating")

    val model: ALSModel = als.fit(df)

    model
  }
}

object ALSModelRecommendForUserSubset {
  def run(model: ALSModel) = {
    // Top 10 recommendations for each of the users in the DF "users"
    // val df: DataFrame = model.recommendForUserSubset(users, 10)

  }
}
