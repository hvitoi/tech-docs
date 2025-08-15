package main

import "math/rand"

func main() {
	source := rand.NewSource(12345)
	randomGenerator := rand.New(source)
	println(randomGenerator.Intn(10))
	println(randomGenerator.Intn(10))
	println(randomGenerator.Intn(10))
}
