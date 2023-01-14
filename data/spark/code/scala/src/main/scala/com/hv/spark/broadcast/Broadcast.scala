package com.hv.spark.Broadcast

import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.spark.broadcast.Broadcast
import org.apache.log4j.Level

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val myMap = Init.run()

    // Instance methods
    BroadcastValue.run(myMap)

  }
}

object Init {
  def run(): Broadcast[Map[String, Int]] = {
    // Create a singleton SparkContext named "MyApp"
    // Run on the local machine and use all cores
    val sc: SparkContext = new SparkContext("local[*]", "MyApp")
    val myMap: Broadcast[Map[String, Int]] =
      sc.broadcast(
        Map("a" -> 1, "b" -> 2)
      )
    myMap
  }
}

object BroadcastValue {
  def run(myMap: Broadcast[Map[String, Int]]) = {
    // This can be run by the driver program at any time to download the item stored in the broadcast
    val myMapValue: Int = myMap.value("a")
  }
}
