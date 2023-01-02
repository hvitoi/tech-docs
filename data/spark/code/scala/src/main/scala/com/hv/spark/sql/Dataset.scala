package com.hv.spark.sql.Dataset

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
    val ds = Init.run()

    /*
     * -> Unit
     */
    DatasetPrintSchema.run(ds)
    DatasetCreateOrReplaceTempView.run(ds)
    DatasetShow.run(ds)

    /*
     * -> RDD
     */
    DatasetRdd.run(ds)

    /*
     * RelationalGroupedDataset
     */
    DatasetGroupBy.run(ds)

    /*
     * -> Dataset
     */
    DatasetFilter.run(ds)
    DatasetSort.run(ds)
    DatasetAlias.run(ds)

    /*
     * -> DataFrame
     */
    DatasetSelect.run(ds)
    DatasetWithColumn.run(ds)

    /*
     * -> Array
     */
    DatasetCollect.run(ds)

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

object DatasetRdd {
  def run(ds: Dataset[Movie]) = {
    // Convert a dataset into a rdd
    ds.rdd
  }
}

object DatasetShow {
  def run(ds: Dataset[Movie]) = {
    // Print the results from a DS
    ds.show() // print first 20 results
    // ds.show(ds.count.toInt) // print all results
  }
}

object DatasetFilter {
  def run(ds: Dataset[Movie]) = {
    // same as SELECT * FROM movies WHERE movieId=1
    val res: Dataset[Movie] =
      ds.filter(ds("movieId") === 1)
    val res2: Dataset[Movie] =
      ds.filter(ds("movieId") =!= 10)
    val res3: Dataset[Movie] =
      ds.filter(ds("movieId") > 10)
  }
}

object DatasetSort {
  def run(ds: Dataset[Movie]) = {
    // return results
    ds.sort()
    // ds.sort("age")
  }
}

object DatasetAlias {
  def run(ds: Dataset[Movie]) = {
    // print results
    val dsWithAlias: Dataset[Movie] = ds.alias("blabla")
  }
}

object DatasetGroupBy {
  def run(ds: Dataset[Movie]) = {
    // same as SELECT * FROM movies GROUP BY genres
    val groupedDs: RelationalGroupedDataset =
      ds.groupBy("genres")
  }
}

object DatasetSelect {
  def run(ds: Dataset[Movie]) = {
    // same as SELECT movieId, genres FROM movies
    val res: DataFrame = ds.select(ds("movieId"), ds("genres"))
    val res2: DataFrame = ds.select(ds("movieId") + 10, ds("genres"))
    val res3: DataFrame = ds
      .select(
        explode(split(ds("genres"), "\\W+"))
          .alias("genres_splitted")
      ) // a new column is created (therefore the return is a DataFrame, because it does not conform with the Dataset schema)

    res3.show()
  }
}

object DatasetWithColumn {
  def run(ds: Dataset[Movie]) = {
    // modify a column with a function
    // a new column can also be added
    val dsWithWithColumn =
      ds.withColumn("movieId", ds("movieId") * 2)
  }
}

object DatasetCollect {
  def run(ds: Dataset[Movie]) = {
    // return results
    ds.collect()
  }
}
