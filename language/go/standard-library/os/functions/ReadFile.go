package main

import (
	"fmt"
	"os"
)

func main() {
	err := os.WriteFile("file.txt", []byte("Hello!"), 0666)

	fileBinary, err := os.ReadFile("file.txt")

	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}

	fmt.Println(string(fileBinary))
}
