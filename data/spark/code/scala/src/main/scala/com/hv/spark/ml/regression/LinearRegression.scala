package com.hv.spark.LinearRegression

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.regression.LinearRegression
import javax.xml.crypto.Data
import org.apache.spark.ml.regression.LinearRegressionModel

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val df = InitDF.run()

    // Static Methods
    val lir = LinearRegressionNew.run()

    // Instance Methods
    LinearRegressionFit.run(lir, df)

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

    val assembler: VectorAssembler =
      new VectorAssembler()
        .setInputCols(Array("features_raw"))
        .setOutputCol("features")

    val wholeDf = assembler
      .transform(df)
      .select("label", "features")
      .randomSplit(Array(0.5, 0.5))

    wholeDf
  }
}

object LinearRegressionNew {
  def run() = {
    // create the model
    val lir: LinearRegression = new LinearRegression()
      .setRegParam(0.3) // regularization
      .setElasticNetParam(0.8) // elastic net mixing
      .setMaxIter(100) // max iterations
      .setTol(1e-6) // convergence tolerance
    lir
  }
}

object LinearRegressionFit {
  def run(lir: LinearRegression, df: Array[DataFrame]) = {
    val trainDf = df(0)

    // train the model
    val model: LinearRegressionModel = lir.fit(trainDf)
  }
}
