package com.hv.spark.sql.Dataframe

import org.apache.spark.sql.Dataset
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.DataFrame
import org.apache.log4j.Logger
import org.apache.log4j.Level

case class Movie(movieId: Int, title: String, genres: String)

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val df = Init.run()

    /*
     * Instance methods
     */
    DataFrameCollect.run(df)
    DataFrameShow.run(df)

  }
}

object Init {
  def run(): DataFrame = {
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
    df
  }
}

object DataFrameCollect {
  def run(df: DataFrame) = {
    // return results
    df.collect()
  }
}

object DataFrameShow {
  def run(df: DataFrame) = {
    // print results
    df.show()
  }
}
