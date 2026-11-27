package main

import (
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

func TestGreet(t *testing.T) {
	store := NewMockUserStore(t) // asserts all expectations were met at the end of the test
	store.EXPECT().GetName(1).Return("Alice", nil).Once()

	got, err := Greeter{store: store}.Greet(1)

	assert.NoError(t, err)
	assert.Equal(t, "Hello, Alice!", got)
}

func TestGreetError(t *testing.T) {
	store := NewMockUserStore(t)
	store.EXPECT().GetName(mock.Anything).Return("", errors.New("not found"))

	_, err := Greeter{store: store}.Greet(42)

	assert.EqualError(t, err, "greet user 42: not found")
}

func TestGreetRunAndReturn(t *testing.T) {
	store := NewMockUserStore(t)
	store.EXPECT().GetName(mock.AnythingOfType("int")).RunAndReturn(func(id int) (string, error) {
		return map[int]string{1: "Alice", 2: "Bob"}[id], nil
	}).Times(2)

	g := Greeter{store: store}
	a, _ := g.Greet(1)
	b, _ := g.Greet(2)

	assert.Equal(t, "Hello, Alice!", a)
	assert.Equal(t, "Hello, Bob!", b)
}
