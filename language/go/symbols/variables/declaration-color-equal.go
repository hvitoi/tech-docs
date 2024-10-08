package main

func main() {
	// "color-equal" syntax can be used only inside of functions
	// It always eaves to the compiler to infer the data type (not possible to set it explicitly)
	// Only for declaring a new variable (no reassign)

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
