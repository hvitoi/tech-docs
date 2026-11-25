package main

import "fmt"

// Interface to writer some data no matter what destination/type it is (e.g., outgoing http request, text file on hd, terminal)
// The input of reader function is always []byte

type myWriter struct{}

func main() {
	writer := myWriter{}
	message := "Hello!"
	writer.Write([]byte(message))
}

func (myWriter) Write(bs []byte) (int, error) { // first return arg is the number of bytes written
	fmt.Println(string(bs))
	return len(bs), nil
}
