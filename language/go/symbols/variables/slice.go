package main

import "fmt"

func main() {
	// A slice has a dynamic size (can grow or shrink)
	// A slice has only one data type and it needs to be defined on the variable declaration

	letters := []string{"a", "b", "c"} // Declare & Assign
	letters = append(letters, "d")     // Reassign
	letters = []string{"x", "y", "z"}  // Reassign

	fmt.Println(letters)
}
