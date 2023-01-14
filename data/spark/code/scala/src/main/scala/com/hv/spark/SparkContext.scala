package com.hv.spark.SparkContext

import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.spark.broadcast.Broadcast
import org.apache.spark.util.LongAccumulator
import org.apache.log4j.Level
// import org.apache.spark._ // not good!

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Static methods
    val sc = SparkContextNew.run()

    // Instance methods
    SparkContextTextFile.run(sc)
    SparkContextBroadcast.run(sc)
    SparkContextLongAccumulator.run(sc)

  }
}

object SparkContextNew {
  def run(): SparkContext = {
    // Create a singleton SparkContext named "MyApp"
    // Run on the local machine and use all cores
    val sc: SparkContext = new SparkContext("local[*]", "MyApp")
    sc
  }
}

object SparkContextTextFile {
  def run(sc: SparkContext) = {
    // Load a text file into an RDD (in SC)
    val lines: RDD[String] = sc.textFile("data/ml-100k/ratings.csv")
  }
}

object SparkContextBroadcast {
  def run(sc: SparkContext) = {
    // used to ship off some data into the driver program as the script starts up
    // This data will be sent to all the executors running the driver program
    val myMap: Broadcast[Map[String, Int]] =
      sc.broadcast(
        Map("a" -> 1, "b" -> 2)
      )
  }
}

object SparkContextLongAccumulator {
  def run(sc: SparkContext) = {
    val myAccumulator: LongAccumulator = sc.longAccumulator("foo")
  }
}
