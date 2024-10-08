package main

import "fmt"

// A "receiver" creates a new method for a given type
type especialString string

func (s especialString) print() {
	// "s" is a copy of the original string
	fmt.Println(s)
}

func (sPointer *especialString) modify(newValue string) {
	// "sPointer" is the pointer to the original list
	*sPointer = especialString(newValue)
}

func main() {
	myName := especialString("Henry")
	myName.print()
	myName.modify("John") // there is no need to cast the "foo" variable into a pointer (go does that transparently)
	myName.print()
}
