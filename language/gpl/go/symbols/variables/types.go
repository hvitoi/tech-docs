package main

import "fmt"

// Go does not have classes, but you can define methods on types

// the new type extends all the behaviors of original type
// The type itself can be used to cast other types. E.g., deck([]string{"a", "b", "c"})

type sliceOfIntegers []int

type person struct {
	firstName string
	lastName  string
}

func main() {
	numbers := sliceOfIntegers{1, 2, 3}
	fmt.Println(numbers)
}
