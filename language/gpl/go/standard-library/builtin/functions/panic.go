package main

// Terminate a program immediately by causing a runtime error

import (
	"fmt"
)

func divide(a, b int) int {
	if b == 0 {
		panic("cannot divide by zero")
	}
	return a / b
}

func main() {

	// allows the program to handle the panic gracefully
	// the deferred function checks if a panic occurred using recover()
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered from panic:", r)
		}
	}()

	result := divide(10, 0) // This will cause a panic
	fmt.Println("Result:", result)
}
