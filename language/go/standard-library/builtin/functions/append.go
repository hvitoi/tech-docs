package main

import "fmt"

func main() {
	letters := []string{"a", "b", "c"}
	letters = append(letters, "d")

	fmt.Println(letters)
}
