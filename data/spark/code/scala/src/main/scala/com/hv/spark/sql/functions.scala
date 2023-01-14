package com.hv.spark.sql.functions

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.sql.Column
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Dataset
import org.apache.spark.sql.RelationalGroupedDataset
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._

case class Movie(movieId: Int, title: String, genres: String)

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val ds = Init.run()

    Explode.run(ds)
    Split.run(ds)
    Round.run(ds)
    Size.run(ds)
    Min.run(ds)
    Avg.run(ds)
    Lower.run(ds)
    Desc.run(ds)
    Udf.run(ds)
    Col.run(ds)

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

object Explode {
  def run(ds: Dataset[Movie]) = {
    // Transforms each column of the data into individual rows
    val res: Column =
      explode(ds("genres"))
  }
}

object Split {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      split(ds("genres"), "\\W+")

    val res2: Column =
      split(col("genres"), "\\W+") // same output

    // The first element from each split with space delimiter
    val res3: Column =
      split(ds("genres"), " ")(0)
  }
}

object Round {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      round(ds("movieId"), 2)
  }
}

object Size {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      size(ds("movieId"))
  }
}

object Min {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      min(ds("movieId"))
  }
}

object Avg {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      avg(ds("movieId"))
  }
}

object Lower {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      lower(ds("genres"))
  }
}

object Desc {
  def run(ds: Dataset[Movie]) = {
    val res: Column =
      desc("genres")
  }
}

object Udf {
  def run(ds: Dataset[Movie]) = {
    // wrap a conventional function as a UserDefinedFunction
    // therefore it can be used just like avg, desc, lower, etc
    // An UDF returns a Column
    val myCustomFunction = (x: Int) => x * x
    val myFn: UserDefinedFunction = udf(myCustomFunction)
  }
}

object Col {
  def run(ds: Dataset[Movie]) = {
    // get the movieId column
    // similar to just use ds("movieId")
    val res: Column =
      col("movieId")
  }
}
