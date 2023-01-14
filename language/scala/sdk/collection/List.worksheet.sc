// List contains values with same type
val foo: List[String] = List("a", "b", "c", "d")

foo(0) // zero-indexed

// iterate through a list
for (el <- foo) { println(el) }

// concatenate lists
foo ++ List("e", "f")

/*
 * contains
 */
val foo2 = List(1, 2, 3)

foo2.contains(3)

/*
 * distinct
 */
val foo3 = List(1, 1, 2, 2, 3)

// only unique values
foo3.distinct

/*
 * filter
 */

val foo4 = List(1, 2, 3)

// List.filter
foo4.filter((x: Int) => x != 2)

foo4.filter(_ != 2) // short syntax

/*
 * foreach
 */

val foo5: List[String] = List("a", "b", "c")

foo5.foreach(println)

/*
 * map
 */
val foo6 = List(1, 2, 3)

foo6.map((num: Int) => { num + 1 })

/*
 * max
 */

val foo7 = List(1, 2, 3)

foo7.max

/*
 * reduce
 */
val foo8 = List(1, 2, 3)

foo8.reduce((sum: Int, item: Int) => sum + item) // sum all numbers

/*
 * reverse
 */
val foo9 = List(1, 2, 3)

foo9.reverse

/*
 * sortBy
 */
val foo10: List[Int] = List(3, 2, 1)

/*
 * sorted
 */
val foo11 = List(2, 1, 3)

foo11.sorted

/*
 * sum
 */
val foo12 = List(1, 2, 3)

foo12.sum

/*
 * head
 */
val foo13 = List(1, 2, 3)

foo13.head // head item

/*
 * tail
 */
val foo14 = List(1, 2, 3)

foo14.tail // remaining items (apart from the head)
