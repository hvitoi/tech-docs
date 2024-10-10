package main

import (
	"fmt"
	"os"
)

// Implements the Reader interface
func main() {
	file, _ := os.Open("file.txt")
	stat(file)
}

func stat(file *os.File) {
	fileStat, _ := file.Stat()
	fmt.Println(fileStat.Size())
}
