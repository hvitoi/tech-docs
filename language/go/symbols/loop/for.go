package main

import "fmt"

func main() {
	letters := []string{"a", "b", "c"}

	for i, letter := range letters {
		fmt.Println(i, letter)
	}

}
