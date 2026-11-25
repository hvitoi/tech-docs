package main

import "fmt"

// Go does not have classes. However, you can define methods on types
// A method is a function with a special receiver argument.
// The type and the method with receiver must be defined in the same package

// A "receiver" creates a new method for a given type
type especialString string

// The receiver appears between the "func" keyword and the method name
func (s especialString) print() {
	// s is passed by value
	fmt.Println(s)
}

// Pointer receiver: allows modifying the original type value
// Pointer receivers are also used in order to avoid copying the value on each method call (more useful if the receiver is a large struct)
func (sPointer *especialString) modify(newValue string) {
	// s is passed by reference (pointer)
	*sPointer = especialString(newValue) // reassign the value of s
}

func main() {
	myName := especialString("Henry")
	myName.print()
	myName.modify("John") // there is no need to cast the "myName" variable into a pointer (go does that transparently). Go interprets myName.modify("...") as (&myName).modify("...") since the method has a pointer receiver
	myName.print()
}
