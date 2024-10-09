package main

import "fmt"

// All the elements in an `array` or `slice` must be of same type!
// Arrays and slices are 0 indexed

func main() {
	// A slice has a dynamic size (can grow or shrink)
	// A slice has only one data type and it needs to be defined on the variable declaration
	// [] tells it's a slice, {} specify the elements
	letters := []string{"a", "b", "c"} // Declare & Assign
	letters = append(letters, "d")     // Reassign
	letters = []string{"x", "y", "z"}  // Reassign

	// Accessing indexes
	fmt.Println(letters[0])

	// Slicing
	fmt.Println(letters[0:2]) // from 0 to 2
	fmt.Println(letters[:2])  // up until 2
	fmt.Println(letters[0:])  // from 0
	fmt.Println(letters[:])   // everything
}
