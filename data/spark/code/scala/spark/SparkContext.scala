//package com.hvitoi.spark

// import org.apache.spark._ // not good!
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.log4j.Level

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Context
    val sc = SparkContextNew.run() // singleton

    // RDD
    val rdd = SparkContextTextFile.run(sc)

    // RDD transforms
    SparkContextMap.run(rdd)

    // RDD actions
    SparkContextCountByValue.run(rdd)
  }
}

object SparkContextNew {
  def run(): SparkContext = {
    // Create a SparkContext named "RatingsCounter"
    // Run on the local machine and use all cores
    val sc: SparkContext = new SparkContext("local[*]", "RatingsCounter")
    sc
  }
}

object SparkContextTextFile {
  def run(sc: SparkContext): RDD[String] = {
    // Load a text file into an RDD (in SC)
    val lines: RDD[String] = sc.textFile("data/ml-100k/ratings.csv")
    lines
  }
}

object SparkContextMap {
  def run(rdd: RDD[String]) = {
    // map each line of the rdd
    // break the strings on the comma and take the 3rd element (the rating start)
    val ratingsString: RDD[String] = rdd.map(x => x.split(",")(2))
  }
}

object SparkContextCountByValue {
  def run(rdd: RDD[String]) = {
    val ratings: RDD[String] = rdd.map(x => x.split(",")(2))

    // count the occurrences of each value in the RDD { "5.0" -> 13, "4.0" -> 8, ...}
    val results = ratings.countByValue()

    // Sort and print results
    val sortedResults = results.toSeq.sortBy(_._1)
    sortedResults.foreach(println)
  }
}
