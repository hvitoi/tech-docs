package main

// Go is a `static typed` language (just like c++ and java)

func main() {
	// "color-equal" syntax can be used only inside of functions
	// It always leaves to the compiler to infer the data type (not possible to set it explicitly)
	// It can only be used when declaring a new variable
	// The variable created using := is mutable
	// Variables declared with := are evaluated at runtime, which allows for more dynamic behavior.

	// single variables
	myName := "Henry"        // Declare & Initialize
	myName = "Henry Awesome" // Assign
	println(myName)

	// Multiple variables
	a, b := "foo", 9
	println(a)
	println(b)

	// Swap variables
	x, y := 1, 2
	y, x = x, y
	println(x)
	println(y)
}
