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

// function with pointers
// With pointers it's possible to modify the original data structure (and not its copy)
func modify(sPointer *string, newValue string) {
	*sPointer = newValue
}

// function multiple possible types
func Add[T int | float64 | ~uint8](a T, b T) T { // accepts byte because it's an alias to uint8
	return a + b
}

// // function multiple possible types
// func Add2[T constraints.Ordered](a T, b T) T { // from "golang.org/x/exp/constraints"
// 	return a + b
// }

// function with generics
func MapValues[T int | float64 | ~uint8](values []T, mapFunc func(T) T) []T {
	var mappedValues []T

	for _, v := range values {
		mappedValues = append(mappedValues, mapFunc(v))
	}

	return mappedValues
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

	// multiple types
	Add(1, 1.5)

	// generics
	result := MapValues([]int{1, 2, 3}, func(n int) int { return n * 2 }) // inline function
	fmt.Println(result)
}
