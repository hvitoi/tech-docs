import scala.Option

// May of may not hold any value
var foo: Option[Int] = None
foo = Option(1)

/*
 * get
 */
val bar: Int = foo.get
