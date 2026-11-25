package main

import (
	"fmt"
	"math"
)

// return 1 value
func greeting(name1, name2 string) string {
	// the received parameters are copies of the original value
	return "Hello " + name1 + ", " + name2 + "!"
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
func add[T int | float64 | ~uint8](a T, b T) T { // accepts byte because it's an alias to uint8
	return a + b
}

// // function multiple possible types
// func Add2[T constraints.Ordered](a T, b T) T { // from "golang.org/x/exp/constraints"
// 	return a + b
// }

// function with generics
func mapValues[T int | float64 | ~uint8](values []T, mapFunc func(T) T) []T {
	var mappedValues []T

	for _, v := range values {
		mappedValues = append(mappedValues, mapFunc(v))
	}

	return mappedValues
}

func namedReturnValues(sum int) (x, y int) {
	x = sum / 2
	y = sum - x
	return // "naked return" (return without args)
}

// Function values
func compute(fn func(float64, float64) float64) float64 {
	return fn(2, 10)
}

// Function closure (a function value that references variables outside its body - it stores a state)
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	greetingMessage := greeting("Henry", "John")
	fmt.Println(greetingMessage)

	userName, userAge := userInfo("Henry", 30)
	fmt.Println(userName)
	fmt.Println(userAge)

	myName := "Henry"
	modify(&myName, "John")
	fmt.Println(myName)

	// multiple types
	add(1, 1.5)

	// named values
	var x, y = namedReturnValues(7)
	fmt.Println(x, y)

	// generics
	result := mapValues([]int{1, 2, 3}, func(n int) int { return n * 2 }) // function literal
	fmt.Println(result)

	// Inline function declaration
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}
