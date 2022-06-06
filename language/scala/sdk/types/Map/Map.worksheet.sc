val shipMap = Map(
  "Kirk" -> "Enterprise",
  "Picard" -> "Enterprise-D",
  "Sisko" -> "Deep Space Nine",
  "Janeway" -> "Voyager"
)

// access a value from a key
shipMap("Janeway")

// try to access a value. With exception handling
val archersShip = util.Try(shipMap("Archer")) getOrElse "Unknown"
