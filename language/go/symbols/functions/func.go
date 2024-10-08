package main

import "fmt"

// return 1 value
func greeting(name string) string {
	// the received parameters are copies of the original value
	return "Hello " + name + "!"
}

// return multiple values
func userInfo(name string, age int) (string, int) {
	// the return are 2 independent values (not a tuple data type)
	return name, age
}

// functions with pointers
// With pointers it's possible to modify the original data structure (and not its copy)
func modify(sPointer *string, newValue string) {
	*sPointer = newValue
}

func main() {
	greetingMessage := greeting("Henry")
	fmt.Println(greetingMessage)

	userName, userAge := userInfo("Henry", 30)
	fmt.Println(userName)
	fmt.Println(userAge)

	myName := "Henry"
	modify(&myName, "John")
	fmt.Println(myName)
}
