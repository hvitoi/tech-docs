var foo = Map(
  "a" -> 1,
  "b" -> 2,
  "c" -> 3,
  "d" -> 4
)

foo("b") // access a value from a key

// try to access a value. With exception handling
util.Try(
  foo("z")
) getOrElse "Unknown"

/*
 * contains
 */
foo.contains("a") // lookup for a key

/*
 * toSeq
 */

// add new item
foo += ("e" -> 5)
// Transform the map into list (seq) of tuples
val seq: Seq[(String, Int)] = foo.toSeq
