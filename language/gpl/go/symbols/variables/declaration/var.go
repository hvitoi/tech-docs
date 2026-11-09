package main

import (
	"fmt"
	"math/cmplx"
)

// Go is a `static typed` language (just like c++ and java)
// Variables created with "var" are evaluated at compile-time. This means their value must be known at the time the program is compiled.
// "var" syntax can be used at "package" or "function" level

func main() {

	// explicit types
	var myName string = "Henry" // Declare & Initialize
	myName = "Henry Awesome"    // Assign
	println(myName)

	// inferred types
	var myName2 = "Henry"     // Declare & Initialize
	myName2 = "Henry Awesome" // Assign
	println(myName2)

	// only declaration
	var myName3 string // Declare and Initialize it with a "zero" value (according to the data type) - 0 for numeric types, false for the boolean type, and "" (the empty string) for strings.
	myName3 = "Henry"  // Assign
	println(myName3)

	// declaring multiple
	var a, b int = 1, 2
	println(a)
	println(b)

	var (
		ToBe   bool       = false
		MaxInt uint64     = 1<<64 - 1
		z      complex128 = cmplx.Sqrt(-5 + 12i)
	)
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}

// Zero Values
//   string ""
//   int    0
//   float  0
//   bool   false
//   nil is a pre-declared identifier representing the zero value for a pointer, channel, func, interface, map, or slice type.

// for structs, each field is created with a zero values according to the data type
