package main

import "fmt"

// Create a new type (a slice of string)
// the new type extends all the behaviors of slice of strings
// The type itself can be used to cast other types. E.g., deck([]string{"a", "b", "c"})
type sliceOfIntegers []int

func main() {
	numbers := sliceOfIntegers{1, 2, 3}
	fmt.Println(numbers)
}
