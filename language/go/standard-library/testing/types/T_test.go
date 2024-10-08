package main

import (
	"testing"
)

func Add(a, b int) int {
	return a + b
}

func TestAdd(t *testing.T) {
	result := Add(1, 1)

	// Errorf
	if result != 2 {
		t.Errorf("Expected 2, but got %d", result)
	}
}
