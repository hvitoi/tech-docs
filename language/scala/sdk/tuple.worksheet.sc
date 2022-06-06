// Data structures

// Tuples
// Immutable lists
val captainStuff = ("Picard", "Enterprise-D", "NCC-1701-D")
println(captainStuff)

// Refer to the individual fields with a ONE-BASED index
println(captainStuff._1)
println(captainStuff._2)
println(captainStuff._3)

// key-value pair (it's actually a tuple with 2 values)
val picardsShip = "Picard" -> "Enterprise-D"
println(picardsShip._2)

// tuple with different value types
val aBunchOfStuff = ("Kirk", 1964, true)
