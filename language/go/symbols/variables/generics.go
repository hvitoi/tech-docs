package main

import "fmt"

type Num interface {
	int | float64 | ~uint8
}

func MapValues[T Num](values []T, mapFunc func(T) T) []T {
	var mappedValues []T
	for _, v := range values {
		mappedValues = append(mappedValues, mapFunc(v))
	}
	return mappedValues
}

type User[T Num] struct {
	ID   int
	Name string
	Data T
}

type CustomMap[T comparable, V int | string] map[T]V // comparable is any type that can be compared with its same type

func main() {
	// function
	result := MapValues([]int{1, 2, 3}, func(n int) int { return n * 2 }) // inline function
	fmt.Println(result)

	// struct
	u := User[int]{
		ID:   9,
		Name: "John",
		Data: 8,
	}
	fmt.Println(u)

	// map
	m := make(CustomMap[int, string])
	m[3] = "3"
}
