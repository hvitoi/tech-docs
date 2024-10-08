package main

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

// for structs, each field is created with a zero values according to the data type
