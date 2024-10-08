package main

import "fmt"

func main() {
	// formatted string
	name := "Henry"
	greeting := fmt.Sprintf("Hello %v", name)
	println(greeting)
}
