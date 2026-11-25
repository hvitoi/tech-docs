package main

import (
	"fmt"
	"io"
	"strings"
)

// Interface to read some data no matter what source/type it is
// The output of reader function is always []byte

// func (T) Read(b []byte) (n int, err error)

func main() {
	var r *strings.Reader = strings.NewReader("Hello, Reader!")

	b := make([]byte, 8)
	for {
		n, err := r.Read(b)
		fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
		fmt.Printf("b[:n] = %q\n", b[:n])
		if err == io.EOF {
			break
		}
	}
}
