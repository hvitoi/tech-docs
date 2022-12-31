package com.hv.spark.rdd.RDD

import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.log4j.Level
// import org.apache.spark._ // not good!

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    val rdd = SparkContextTextFile.run()

    /*
     * RDD transforms
     */

    RDDMap.run(rdd)
    RDDFlatMap.run(rdd)
    RDDFilter.run(rdd)
    RDDMapValues.run(rdd) // tuple rdd only
    RDDReduceByKey.run(rdd) // tuple rdd only
    RDDSortByKey.run(rdd) // tuple rdd only

    /*
     * RDD actions
     */

    RDDCollect.run(rdd)
    RDDCountByValue.run(rdd)
  }
}

object SparkContextTextFile {
  def run(): RDD[String] = {
    // Create a singleton SparkContext named "MyApp"
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
    val transformedRdd: RDD[String] = rdd.map(x => x.split(",")(1))
  }
}

object RDDFlatMap {
  def run(rdd: RDD[String]) = {
    // FlatMap can return any number of output (Array of rows) rows for one input row
    // Differently from "map" in which the relation is 1 to 1
    val transformedRdd: RDD[String] = rdd.flatMap(x => x.split(" "))
  }
}

object RDDFilter {
  def run(rdd: RDD[String]) = {

    val transformedRdd: RDD[String] = rdd.filter(x => x == "Batman")
  }
}

object RDDMapValues {
  def run(rdd: RDD[String]) = {
    val tupleRdd: RDD[(String, Int)] = rdd.map(x => (x, 1))

    val transformedRdd: RDD[(String, Int)] = tupleRdd.mapValues(x => x + 1)
  }
}

object RDDReduceByKey {
  def run(rdd: RDD[String]) = {
    val tupleRdd: RDD[(String, Int)] = rdd.map(x => (x, 1))

    // Reduce only duplicated keys
    // E.g., a -> 1, a -> 2, b -> 3 --- a -> 3, b -> 3
    // Final output is do have unique keys only (the duplicated ones are reduced)
    val transformedRdd: RDD[(String, Int)] =
      tupleRdd.reduceByKey((val1, val2) => val1 + val2)

    // map + reduceByKey is commonly used to count values (alternative to countByValue)
    // first it maps each value into (x, 1) then reduce by key summing up each identical key (x, y) => x + y
  }
}

object RDDSortByKey {
  def run(rdd: RDD[String]) = {
    val tupleRdd: RDD[(String, Int)] = rdd.map(x => (x, 1))

    // sorts by the tuple key (x._1)
    val transformedRdd: RDD[(String, Int)] = tupleRdd.sortByKey()
  }
}

object RDDCollect {
  def run(rdd: RDD[String]) = {
    val result: Array[String] = rdd.collect()

  }
}

object RDDCountByValue {
  def run(rdd: RDD[String]) = {
    // count the occurrences of each value in the RDD
    val result: scala.collection.Map[String, Long] = rdd.countByValue()

    // result.toSeq.sortBy(_._1).foreach(println)
  }
}
