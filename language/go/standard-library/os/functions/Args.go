package main

import (
	"fmt"
	"os"
)

func main() {
	// Access to the list of command-line arguments passed to the program
	absolutePath := os.Args[0] // Absolute path of the generated binary that is being executed
	firstArg := os.Args[1]
	secondArg := os.Args[2]
	fmt.Println(absolutePath)
	fmt.Println(firstArg)
	fmt.Println(secondArg)
}
