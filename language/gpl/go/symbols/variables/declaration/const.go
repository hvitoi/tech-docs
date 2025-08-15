package main

import "fmt"

// similar to "var", but variables created with "const" cannot be changed
// Constants are evaluated at compile-time. This means their value must be known at the time the program is compiled.

const pi float64 = 3.14159               // set types explicitly
const apiURL = "https://httpbin.org/get" // infer types

func main() {

	fmt.Println("The value of pi is:", pi)
	// pi = 3.14 // This would cause an error because pi is a constant
}
