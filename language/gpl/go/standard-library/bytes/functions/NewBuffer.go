package main

import (
	"bytes"
	"fmt"
)

func main() {
	data := "Hello!"
	buffer := bytes.NewBuffer([]byte(data))

	fmt.Print(buffer)
}
