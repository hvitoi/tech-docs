package main

import (
	"fmt"
	"os"
)

// Implements the Reader interface
func main() {
	var file *os.File
	var err error
	file, err = os.Open("file.txt")

	if err != nil {
		os.Exit(1)
	}

	fmt.Println(file)
}
