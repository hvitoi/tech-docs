val foo = Map(
  "a" -> 1,
  "b" -> 2,
  "c" -> 3,
  "d" -> 4
)

// Transform the map into list (seq) of tuples
val seq: Seq[(String, Int)] = foo.toSeq
