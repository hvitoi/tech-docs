package com.hv.spark.SparkContext

import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.log4j.Level
// import org.apache.spark._ // not good!

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Static methods
    val sc = SparkContextNew.run()

    // Instance methods
    SparkContextTextFile.run(sc)

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
