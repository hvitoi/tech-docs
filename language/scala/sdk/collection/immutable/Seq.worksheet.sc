import scala.collection.immutable.Seq
import scala.Seq // same

val foo1: Seq[String] = Seq("a", "b", "c")

/*
 * foreach
 */
val foo2: Seq[String] = Seq("c", "a", "b")

foo2.foreach(println)

/*
 * sortBy
 */
val foo3: Seq[String] = Seq("c", "a", "b")
val bar3: Seq[String] = foo3.sortBy(x => x)
