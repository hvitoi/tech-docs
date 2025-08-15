package main

import (
	"io"
	"os"
)

func main() {
	file, err := os.Open("file.txt")

	if err != nil {
		os.Exit(1)
	}

	// copy file to stdout
	io.Copy(os.Stdout, file)
}
