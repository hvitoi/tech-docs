package main

import (
	"fmt"
	"testing"
)

func Add(a, b int) int {
	return a + b
}

func main() {
	fmt.Println(Add(1, 1))
}

func TestAdd(t *testing.T) {
	result := Add(1, 1)
	if result != 2 {
		t.Errorf("Expected 2, but got %d", result)
	}
}
