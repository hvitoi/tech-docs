package main

import "fmt"

func main() {
	data := "Hello!"
	serialized_data := []byte(data) // cast a string into an slice of bytes (ascii character code)

	fmt.Println(serialized_data)
}
