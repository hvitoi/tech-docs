package com.hv.spark.sql.RelationalGroupedDataset

import org.apache.spark.sql.Dataset
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.RelationalGroupedDataset
import org.apache.log4j.Logger
import org.apache.log4j.Level

case class Movie(movieId: Int, title: String, genres: String)

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val groupedDs = Init.run()

    /*
     * Instance methods
     */
    RelationalGroupedDatasetCount.run(groupedDs)

  }
}

object Init {
  def run(): RelationalGroupedDataset = {
    val ss: SparkSession = SparkSession
      .builder()
      .appName("MyApp")
      .master("local[*]")
      .getOrCreate()
    import ss.implicits._
    val ds: Dataset[Movie] = ss.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("ml-latest-small/movies.csv")
      .as[Movie]
    val groupedDs: RelationalGroupedDataset =
      ds.groupBy("genres")
    groupedDs
  }

}

object RelationalGroupedDatasetCount {
  def run(groupedDs: RelationalGroupedDataset) = {
    val result: DataFrame = groupedDs.count()
    result.show()
  }
}
