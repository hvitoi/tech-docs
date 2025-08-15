package main

// Go is a `static typed` language (just like c++ and java)
// Variables created with "var" are evaluated at compile-time. This means their value must be known at the time the program is compiled.

func main() {
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
	var myName3 string // Declare and Initialize it with a "zero" value (according to the data type)
	myName3 = "Henry"  // Assign
	println(myName3)

	// declaring multiple
	var a, b int = 1, 2
	println(a)
	println(b)
}

// Zero Values
//   string ""
//   int    0
//   float  0
//   bool   false
//   nil is a pre-declared identifier representing the zero value for a pointer, channel, func, interface, map, or slice type.

// for structs, each field is created with a zero values according to the data type
