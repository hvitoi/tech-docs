package main

func modify(sPointer *string, newValue string) {
	*sPointer = newValue
}

func main() {
	myName := "Henry"
	pMyName := &myName // pointer to myName (memory address)

	println(*pMyName) // extract the pointer's underlying value (dereferencing)
	modify(pMyName, "Henrique")
	println(*pMyName)
}
