package main

import "fmt"

// creates an empty reference
// only works with slice, map or channel

func main() {

	// Map
	colors := make(map[string]string)
	var colors2 map[string]string // same!
	fmt.Println(colors, colors2)

	// Flexible map
	my_map := make(map[string]interface{})
	fmt.Println(my_map)

	// Slice (creates zeroed array and returns the slice that refers to it)
	bs := make([]byte, 9) // an empty byte slice of size 9
	fmt.Println(bs)

}
