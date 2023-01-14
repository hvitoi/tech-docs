import java.lang.String
//import scala.String // String is actually a type defined inside of scala.String therefore it cannot be imported like this

/*
 * length
 */
val foo1: String = "abc"
val bar1: Int = foo1.length

/*
 * reverse
 */
val foo2: String = "abc"
foo2.reverse

/*
 * split
 */
val foo3: String = "a,b,c"
val bar3: Array[String] = foo3.split(",")
val baz3: Array[String] = foo3.split("\\W+") // split entire words (regex)

/*
 * toFloat
 */
val foo4: String = "12.1"
val bar4: Float = foo4.toFloat

/*
 * toInt
 */
val foo5: String = "12"
val bar5: Int = foo5.toInt

/*
 * toLowerCase
 */
val foo6: String = "ABC"
val bar6: String = foo6.toLowerCase()

/*
 * toUpperCase
 */
val foo7: String = "abc"
val bar7: String = foo7.toUpperCase()
