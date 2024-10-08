package main

func main() {
	varSyntax()
	colonEqualSyntax()
}

func varSyntax() {
	// "var" syntax can be used inside and outside of functions

	// explicit types
	var myName string = "Henry" // Declare & Initialize
	myName = "Henry Awesome"    // Assign
	println(myName)

	// inferred types
	var myName2 = "Henry"     // Declare & Initialize
	myName2 = "Henry Awesome" // Assign
	println(myName2)

	// only declaration
	var myName3 string // Declare and Initialize it with "" (empty string)
	myName3 = "Henry"  // Assign
	println(myName3)

	// declaring multiple
	var a, b int = 1, 2
	println(a)
	println(b)

}

func colonEqualSyntax() {
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
