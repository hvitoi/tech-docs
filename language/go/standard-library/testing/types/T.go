package main

import (
	"fmt"
	"testing"
)

func Add(a, b int) int {
	return a + b
}

func main() {
	fmt.Println(Add(5, 3))
}

func TestAdd(t *testing.T) {
	result := Add(5, 3)
	if result != 8 {
		t.Errorf("Expected 8, but got %d", result)
	}
}
