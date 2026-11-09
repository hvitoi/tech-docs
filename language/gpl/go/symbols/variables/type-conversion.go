package main

import "fmt"

func main() {

	var i int = 42
	var f float64 = float64(i)
	var u uint = uint(f)

	// to slice of bytes
	serialized_data := []byte("Hello") // cast a string into an slice of bytes (ascii character code)
	fmt.Println(serialized_data)

	// to string
	serialized_data2 := string(99) // produces "c", since 99 is the unicode code for "c"
	fmt.Println(serialized_data2)
}
