package com.hv.spark.VectorAssembler

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.SparkSession

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val df = InitDF.run()

    // Static Methods
    val assembler = VectorAssemblerNew.run()

    // Instance Methods
    VectorAssemblerTransform.run(assembler, df)

  }
}

object InitDF {
  def run() = {
    val ss: SparkSession = SparkSession
      .builder()
      .appName("MyApp")
      .master("local[*]")
      .getOrCreate()
    import ss.implicits._
    val df: DataFrame = ss.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("ml-latest-small/movies.csv")
    df
  }
}

object VectorAssemblerNew {
  def run() = {
    val assembler: VectorAssembler =
      new VectorAssembler()
        .setInputCols(Array("features_raw")) // the array of features
        .setOutputCol("features") // as a new column
    assembler
  }
}

object VectorAssemblerTransform {
  def run(assembler: VectorAssembler, df: DataFrame) = {
    val newDf = assembler
      .transform(df)
      .select("label", "features")

    val wholeDf = newDf.randomSplit(Array(0.5, 0.5))
    val trainDf = wholeDf(0)
    val testDf = wholeDf(1)
  }
}
