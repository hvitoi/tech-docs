// at each iteration a new value to assigned to x
// x receives 1, 2, 3
for (x <- 1 to 3) {
  val squared = x * x
  println(squared)
}

// Iterate through a list
val shipList = List("Enterprise", "Defiant", "Voyager", "Deep Space Nine")

for (ship <- shipList) {
  println(ship)
}
