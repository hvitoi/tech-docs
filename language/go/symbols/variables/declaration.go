package main

import "fmt"

// Declaration & Assignment
func main() {
	// var syntax with explicit types
	var myName string = "Henry" // Declare & Assign
	myName = "Henry Awesome"    // Reassign
	fmt.Println(myName)

	// var syntax with implicit types
	var myName2 = "Henry"     // Declare & Assign
	myName2 = "Henry Awesome" // Reassign
	fmt.Println(myName2)

	// Colon-equal syntax: leave to the compiler to infer the data type
	// This syntax is only possible when DECLARING a new variable
	myName3 := "Henry"        // Declare & Assign
	myName3 = "Henry Awesome" // Reassign
	fmt.Println(myName3)
}
