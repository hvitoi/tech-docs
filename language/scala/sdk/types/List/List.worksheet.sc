// Lists
// Must contain values with same type

val shipList = List("Enterprise", "Defiant", "Voyager", "Deep Space Nine")

// zero-indexed
println(shipList(1))
println(shipList.head) // head item
println(shipList.tail) // remaining items (apart from the head)

// iterate through a list
for (ship <- shipList) { println(ship) }

// Concatenate lists
val moreShips = List("Starship")
val lotsOfShips = shipList ++ moreShips
