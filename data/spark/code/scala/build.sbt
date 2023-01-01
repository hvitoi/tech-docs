name := "my-snippets"
version := "0.1.0-SNAPSHOT"
scalaVersion := "2.12.12"
libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.3.1",
  "org.apache.spark" %% "spark-sql" % "3.3.1",
  "org.apache.spark" %% "spark-mllib" % "3.3.1",
  "org.apache.spark" %% "spark-streaming" % "3.3.1"
)
