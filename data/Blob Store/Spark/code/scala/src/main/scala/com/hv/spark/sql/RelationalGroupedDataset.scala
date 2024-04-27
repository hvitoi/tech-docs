package com.hv.spark.sql.RelationalGroupedDataset

import org.apache.spark.sql.Dataset
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.RelationalGroupedDataset
import org.apache.spark.sql.functions._
import org.apache.log4j.Logger
import org.apache.log4j.Level

case class Movie(movieId: Int, title: String, genres: String)

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val groupedDs = Init.run()

    /*
     * -> DataFrame
     */
    RelationalGroupedDatasetCount.run(groupedDs)
    RelationalGroupedDatasetMin.run(groupedDs)
    RelationalGroupedDatasetSum.run(groupedDs)
    RelationalGroupedDatasetAvg.run(groupedDs)
    RelationalGroupedDatasetAgg.run(groupedDs)

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
    val res: DataFrame = groupedDs.count()
  }
}

object RelationalGroupedDatasetMin {
  def run(groupedDs: RelationalGroupedDataset) = {
    val res: DataFrame = groupedDs.min()
  }
}

object RelationalGroupedDatasetSum {
  def run(groupedDs: RelationalGroupedDataset) = {
    val res: DataFrame = groupedDs.sum()
  }
}

object RelationalGroupedDatasetAvg {
  def run(groupedDs: RelationalGroupedDataset) = {
    val res: DataFrame = groupedDs.avg()
    // val res: DataFrame = groupedDs.avg("age")
  }
}

object RelationalGroupedDatasetAgg {
  def run(groupedDs: RelationalGroupedDataset) = {
    // agg creates a new column with the aggregated data
    val res: DataFrame =
      groupedDs
        .agg(round(avg("movieId"), 2))
        .alias("the_rounded_avg")
  }
}
