package main

import "fmt"

type sliceOfStrings []string

// A "receiver" creates a new method for a given type
func (s sliceOfStrings) print() {
	for i, el := range s {
		fmt.Println(i, el)
	}
}

func main() {
	my_var := sliceOfStrings{"a", "b", "c"}
	my_var.print()
}
