package main

import (
	"fmt"
	"os"
)

func main() {
	filename := "file.txt"
	data := "content to be saved"
	serialized_data := []byte(data) // data is casted to a slice of bytes

	// file is created if it does not exist (with the defined permissions)
	// err is null if save is successful
	err := os.WriteFile(filename, serialized_data, 0666)

	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
}
