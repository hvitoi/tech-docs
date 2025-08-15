package main

import "fmt"

func main() {
	// creates an empty reference
	// only works with slice, map or channel

	colors := make(map[string]string)
	// var colors map[string]string // same!

	fmt.Println(colors)

	// an empty byte slice of size 99999
	bs := make([]byte, 99999)
	fmt.Println(bs)

	// flexible map
	my_map := make(map[string]interface{})
	fmt.Println(my_map)

}
