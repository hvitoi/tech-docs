package main

import "os"

func main() {
	filename := "file.txt"
	data := "content to be saved"
	serialized_data := []byte(data) // data is casted to a slice of bytes

	os.WriteFile(filename, serialized_data, 0666) // file is created if it does not exist
}
