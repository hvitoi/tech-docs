package com.hv.spark.StreamingContext

import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds

// This API is mostly superseded
// Use sparksession.readStream to create a structured streaming instead

object Main {
  def main(args: Array[String]) {
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Static methods
    val ssc = StreamingContextNew.run()

    // Instance methods
    StreamingContextCheckpoint.run(ssc)
    StreamingContextStart.run(ssc)
    StreamingContextAwaitTermination.run(ssc)

  }
}

object StreamingContextNew {
  def run() = {
    // Pool for data every 1 second
    val ssc: StreamingContext =
      new StreamingContext("local[*]", "MyApp", Seconds(1))
    ssc
  }
}

object StreamingContextCheckpoint {
  def run(ssc: StreamingContext) = {
    ssc.checkpoint("/home/a")
  }
}

object StreamingContextStart {
  def run(ssc: StreamingContext) = {
    ssc.start()
  }
}

object StreamingContextAwaitTermination {
  def run(ssc: StreamingContext) = {
    ssc.awaitTermination()
  }
}
