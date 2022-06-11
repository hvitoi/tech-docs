val foo = Map(
  "a" -> 1,
  "b" -> 2,
  "c" -> 3,
  "d" -> 4
)

// access a value from a key
val res: Int = foo("b")

// try to access a value. With exception handling
val archersShip = util.Try(foo("z")) getOrElse "Unknown"
