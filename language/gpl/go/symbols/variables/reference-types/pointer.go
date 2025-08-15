package main

func modify(sPointer *string, newValue string) {
	*sPointer = newValue
}

func main() {
	myName := "Henry"
	modify(&myName, "John") // &myName returns a pointer, which is the memory address of the variable "myName"
	println(myName)
}
