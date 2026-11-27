package main

import (
	"errors"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/mock"
)

type MockUserStore struct {
	mock.Mock
}

func (m *MockUserStore) GetName(id int) (string, error) {
	args := m.Called(id)
	return args.String(0), args.Error(1)
}

func TestGreet(t *testing.T) {
	store := new(MockUserStore)
	store.On("GetName", 1).Return("Alice", nil).Once()

	got, err := Greeter{store: store}.Greet(1)

	assert.NoError(t, err)
	assert.Equal(t, "Hello, Alice!", got)
	store.AssertExpectations(t)
}

func TestGreetError(t *testing.T) {
	store := new(MockUserStore)
	store.On("GetName", mock.Anything).Return("", errors.New("not found"))

	_, err := Greeter{store: store}.Greet(42)

	assert.EqualError(t, err, "greet user 42: not found")
	store.AssertCalled(t, "GetName", 42)
}

func TestGreetMatchedBy(t *testing.T) {
	store := new(MockUserStore)
	store.On("GetName", mock.MatchedBy(func(id int) bool { return id > 0 })).Return("Alice", nil)
	store.On("GetName", mock.MatchedBy(func(id int) bool { return id <= 0 })).Return("", errors.New("invalid id"))

	g := Greeter{store: store}
	_, err1 := g.Greet(1)
	_, err2 := g.Greet(-1)

	assert.NoError(t, err1)
	assert.Error(t, err2)
	store.AssertNumberOfCalls(t, "GetName", 2)
}

// Run: side effects on the call arguments
func TestGreetRun(t *testing.T) {
	var seen []int
	store := new(MockUserStore)
	store.On("GetName", mock.AnythingOfType("int")).
		Run(func(args mock.Arguments) { seen = append(seen, args.Int(0)) }).
		Return("Bob", nil)

	g := Greeter{store: store}
	g.Greet(1)
	g.Greet(2)

	assert.Equal(t, []int{1, 2}, seen)
	store.AssertNotCalled(t, "GetName", 3)
}
