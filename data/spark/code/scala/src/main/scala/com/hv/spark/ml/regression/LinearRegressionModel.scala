package com.hv.spark.LinearRegressionModel

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.regression.LinearRegressionModel

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)
    val df = InitDF.run()
    val model = InitModel.run(df(0))

    // Instance Methods
    LinearRegressionModelTransform.run(model, df(1))

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

object InitModel {
  def run(trainDf: DataFrame) = {
    val lir: LinearRegression = new LinearRegression()
      .setRegParam(0.3)
      .setElasticNetParam(0.8)
      .setMaxIter(100)
      .setTol(1e-6)

    val model: LinearRegressionModel = lir.fit(trainDf)

    model
  }
}

object LinearRegressionModelTransform {
  def run(model: LinearRegressionModel, testDf: DataFrame) = {

    // Predict values using the test data
    val fullPredictions: DataFrame = model.transform(testDf)

  }
}
