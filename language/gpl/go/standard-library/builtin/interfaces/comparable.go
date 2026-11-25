package main

// comparable is any type that can be compared with its same type
// makes it possible to use the == and != operators

type CustomMap[T comparable, V int | string] map[T]V

func main() {
	m := make(CustomMap[int, string])
	m[3] = "3"
}
