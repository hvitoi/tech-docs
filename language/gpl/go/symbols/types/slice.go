package main

import "fmt"

// A slice is very similar to an array, but it is dynamically-sized
// The difference on the declaration of a array vs. slice is that on a slice the size is omitted
// A slice does not store any data, it just describes a section of an underlying array.

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

	// Slice properties
	fmt.Println(len(letters))
	fmt.Println(cap(letters))

	// Matrices (slice of slices)
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}
	fmt.Printf("%s", board)

	// Append
	// If the backing array of s is too small to fit all the given values a bigger array will be allocated. The returned slice will point to the newly allocated array.
	var s []int
	s = append(s, 0)          // the result is a new slice containing all the original slice + the new element
	s = append(s, 1, 2, 3, 4) // add multiple
}
