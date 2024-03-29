import scala.Tuple

// Tuple is an immutable list
val captainStuff: (String, String, String) =
  ("Picard", "Enterprise-D", "NCC-1701-D")

// Refer to the individual fields with a ONE-BASED index
captainStuff._1
captainStuff._2
captainStuff._3

// Tuple key-value pair (it's actually a tuple with 2 values)
val picardsShip: (String, String) = "Picard" -> "Enterprise-D"
picardsShip._2

// tuple with different value types
val aBunchOfStuff: (String, Int, Boolean) = ("Kirk", 1964, true)
