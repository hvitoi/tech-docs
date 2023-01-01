package com.hv.spark.sql.Dataset

import org.apache.spark.sql.Dataset
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.RelationalGroupedDataset
import org.apache.log4j.Logger
import org.apache.log4j.Level

case class Movie(movieId: Int, title: String, genres: String)

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val ds = Init.run()

    /*
     * Aux methods
     */
    DatasetPrintSchema.run(ds)
    DatasetCreateOrReplaceTempView.run(ds)
    DatasetShow.run(ds)

    /*
     * Queries
     */
    DatasetFilter.run(ds)
    DatasetGroupBy.run(ds)

    /*
     * Actions
     */
    // DataSetSelect.run()
    // DataSetRdd.run()

  }
}

object Init {
  def run(): Dataset[Movie] = {
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
    ds
  }
}

object DatasetPrintSchema {
  def run(ds: Dataset[Movie]) = {
    // print the dataset's schema (the movie schema)
    ds.printSchema()
  }
}

object DatasetCreateOrReplaceTempView {
  def run(ds: Dataset[Movie]) = {
    // Create a temporary view of the data (similar to SQL views)
    // The view is created based on a dataset
    // The new view will be treated as a SQL table
    ds.createOrReplaceTempView("movies")
  }
}

object DatasetShow {
  def run(ds: Dataset[Movie]) = {
    // Print the results from a DS
    ds.show()
  }
}

object DatasetFilter {
  def run(ds: Dataset[Movie]) = {
    val filteredDs: Dataset[Movie] =
      ds.filter(ds("movieId") === 1)
    filteredDs.show()
  }
}

object DatasetGroupBy {
  def run(ds: Dataset[Movie]) = {
    val groupedDs: RelationalGroupedDataset =
      ds.groupBy("genres")
  }
}
