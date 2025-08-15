import scala.io.Source
import scala.io.BufferedSource

val lines: BufferedSource = Source.fromFile("../.gitignore")

// close the buffer
lines.close()
