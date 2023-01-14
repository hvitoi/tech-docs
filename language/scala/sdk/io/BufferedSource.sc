import scala.io.Source
import scala.io.BufferedSource

val lines: BufferedSource = Source.fromFile("../.gitignore")

// getLines
for (line <- lines.getLines()) {
  println(line)
}
