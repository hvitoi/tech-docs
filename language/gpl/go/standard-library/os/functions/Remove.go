package main

import (
	"fmt"
	"os"
)

func main() {
	os.WriteFile("file.txt", []byte("Hello!"), 0666)

	err := os.Remove("file.txt")

	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
}
