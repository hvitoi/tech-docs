val foo = Map(
  "a" -> 1,
  "b" -> 2,
  "c" -> 3,
  "d" -> 4
)

// access a value from a key
foo("b")

// try to access a value. With exception handling
util.Try(
  foo("z")
) getOrElse "Unknown"
