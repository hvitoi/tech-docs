package com.hv.spark.LongAccumulator

import org.apache.spark.rdd.RDD
import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.spark.broadcast.Broadcast
import org.apache.log4j.Level
import org.apache.spark.util.LongAccumulator

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val myMap = Init.run()

    // Instance methods

  }
}

object Init {
  def run() = {
    val sc: SparkContext = new SparkContext("local[*]", "MyApp")
    val accumulator: LongAccumulator = sc.longAccumulator("foo")
    accumulator
  }
}
