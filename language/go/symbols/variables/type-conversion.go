package main

import "fmt"

func main() {

	// to slice of bytes
	serialized_data := []byte("Hello") // cast a string into an slice of bytes (ascii character code)
	fmt.Println(serialized_data)

	// to string
	serialized_data2 := string(99) // produces "c", since 99 is the unicode code for "c"
	fmt.Println(serialized_data2)
}
