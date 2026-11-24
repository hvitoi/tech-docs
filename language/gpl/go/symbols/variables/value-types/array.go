package main

import "fmt"

// All the elements in an `array` or `slice` must be of same type!
// Arrays and slices are 0 indexed

// An array is a primitive data structure in Go
// Arrays have fixed length

// For a dynamically-sized array, see "slice"

func main() {

	// Array iniatialization
	var arr = [5]string{"a", "b", "c"}
	var arr2 = [...]string{"a", "b", "c"} // Array size inference (Go can't infer the type)
	var arr3 [2]string
	arr4 := [...]string{"a"}
	fmt.Println(arr)
	fmt.Println(arr2)
	fmt.Println(arr3)
	fmt.Println(arr4)

	// Modifying elements
	arr3[0] = "Hello"
	arr3[1] = "World"

	// Accessing elements
	fmt.Println(arr3[1])

	// Create an slice out of an array
	// Slices are like references to arrays
	mySlice := arr[0:2] // the size disappears and becomes dynamic
	mySlice[0] = "z"
	fmt.Println(arr) // the original arr is modified

}
