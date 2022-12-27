// Lists contain values with same type
val foo: List[String] = List("a", "b", "c", "d")

// zero-indexed
foo(0)
foo.head // head item
foo.tail // remaining items (apart from the head)

// iterate through a list
for (el <- foo) { println(el) }

// concatenate lists
foo ++ List("e", "f")
