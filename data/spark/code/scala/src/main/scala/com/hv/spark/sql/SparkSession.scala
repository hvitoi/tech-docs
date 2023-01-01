package com.hv.spark.sql.SparkSession

import org.apache.spark.sql.Dataset
import org.apache.spark.sql.SparkSession
import org.apache.log4j.Logger
import org.apache.log4j.Level

// For Datasets, the schema has to be defined at compile time, therefore a case class must be defined before
case class Movie(movieId: Int, title: String, genres: String)

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    /*
     * Static methods
     */
    val ss = SparkSessionBuilder.run()

    /*
     * Instance methods
     */
    SparkSessionRead.run(ss)
    SparkSessionStop.run(ss)
    SparkSessionSql.run(ss)

  }
}

object SparkSessionBuilder {
  def run(): SparkSession = {
    // The Session object is a representation of an SQL database
    // Create a singleton SparkSession named "MyApp"
    val ss: SparkSession = SparkSession
      .builder()
      .appName("MyApp")
      .master("local[*]")
      .getOrCreate() // create or reused an existing one
    ss
  }

}

object SparkSessionRead {
  def run(ss: SparkSession) = {
    // import from an object
    // make scala implicit infer a schema
    import ss.implicits._
    // read from file
    ss.read
      .option("header", "true") // the document has a header row
      .option("inferSchema", "true") // match class attrs with headers
      .csv("ml-latest-small/movies.csv") // creates DF
      .as[Movie] // converts the DF into a DS
      .createOrReplaceTempView("movies")
  }
}

object SparkSessionStop {
  def run(ss: SparkSession) = {
    ss.stop()
  }
}

object SparkSessionSql {
  def run(ss: SparkSession) = {
    // SQL-like query to the entire SQL database
    ss.sql(
      "SELECT * " +
        "FROM movies " +
        "WHERE genres " +
        "LIKE '%Adventure%'"
    )
  }
}
