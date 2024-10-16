package com.hv.spark.sql.SparkSession

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Dataset
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.IntegerType
import org.apache.spark.sql.types.StringType
import org.apache.spark.sql.types.StructType

// For Datasets, the schema has to be defined at compile time, therefore a case class must be defined before
// The case class defines the schema of the table
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
    SparkSessionSparkContext.run(ss)
    SparkSessionRead.run(ss)
    SparkSessionReadStream.run(ss)
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

    // read from text file
    ss.read.text("ml-latest-small/README.txt")

    // read from csv (schemas inferred)
    ss.read
      .option("header", "true") // the document has a header row
      // .option("sep", "\t") // tab delimiter
      // .option("sep", " ") // space delimiter (does not consider squads inside of quotation marks)
      .option("inferSchema", "true") // match class attrs with headers
      .csv("ml-latest-small/movies.csv") // creates DF
      .as[Movie] // converts the DF into a DS
      .createOrReplaceTempView("movies")

    // read from csv (schemas explicit)
    val movieSchema = new StructType()
      .add("movieId", IntegerType, nullable = true)
      .add("title", StringType, nullable = true)
      .add("genres", StringType, nullable = false)

    ss.read
      .schema(movieSchema)
      .csv("ml-latest-small/movies.csv")
      .as[Movie]
      .createOrReplaceTempView("movies")

  }
}

object SparkSessionReadStream {
  def run(ss: SparkSession) = {

    // read a stream of data
    // the stream is just like a conventional dataset
    // this Dataset increases constantly

    val streamDfJson: DataFrame = ss.readStream
      .json("s3://logs")

    val streamDfText: DataFrame = ss.readStream
      .text("s3://logs")

  }
}

object SparkSessionSparkContext {
  def run(ss: SparkSession) = {
    val sc: SparkContext = ss.sparkContext
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
