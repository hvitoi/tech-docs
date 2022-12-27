val myInt: Int = 1
val myFloat: Float = 3.14159265f

println("Concatenate things: " + myInt + myFloat)
println({ val x = 10; x + 20 }) // in an expression, the last value is returned

// s: substituting
println(s"s prefix to use variables like $myInt")
println(s"s prefix can be used with any expression. Like ${1 + 2}")

// f: formatting
println(f"Pi is about $myFloat%.3f")
println(f"Zero padding on the left: $myInt%05d")
