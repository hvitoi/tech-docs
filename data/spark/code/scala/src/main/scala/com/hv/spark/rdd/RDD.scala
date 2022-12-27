package com.hv.spark.rdd.RDD

import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.log4j.Level
// import org.apache.spark._ // not good!

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val rdd = RDDNew.run() // singleton

    // RDD transforms
    RDDMap.run(rdd)

    // RDD actions
    RDDCountByValue.run(rdd)
  }
}

object RDDNew {
  def run(): RDD[String] = {
    // Create a SparkContext named "MyApp"
    // Run on the local machine and use all cores
    val sc: SparkContext = new SparkContext("local[*]", "MyApp")
    val rdd: RDD[String] = sc.textFile("ml-latest-small/movies.csv")
    rdd
  }
}

object RDDMap {
  def run(rdd: RDD[String]) = {
    // map each line of the rdd
    // break the strings on the comma and take the 2nd element (the rating start)
    val ratingsString: RDD[String] = rdd.map(x => x.split(",")(1))
  }
}

object RDDCountByValue {
  def run(rdd: RDD[String]) = {
    val ratings: RDD[String] = rdd.map(x => x.split(",")(1))

    // count the occurrences of each value in the RDD
    // Returns a Map[String,Long]
    val results = ratings.countByValue()

    // print
    results.toSeq.sortBy(_._1).foreach(println)
  }
}
