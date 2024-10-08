package main

import "fmt"

func main() {
	// An array is a primitive data structure in Go
	// Arrays have fixed length

	var arr = [5]string{"a", "b", "c"}
	fmt.Println(arr)

	arr2 := [...]string{"a", "b", "c"} // Go will infer the size
	fmt.Println(arr2)
}
