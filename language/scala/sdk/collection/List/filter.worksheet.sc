val foo = List(1, 2, 3)

// List.filter
foo.filter((x: Int) => x != 2)

foo.filter(_ != 2) // short syntax
