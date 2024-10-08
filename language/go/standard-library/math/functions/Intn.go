package main

import "math/rand"

func main() {
	// uses a random seed if you don't specify a seed
	randomNumber := rand.Intn(10) // [0,10)
	println(randomNumber)

	// you can also use a fixed seed
	source := rand.NewSource(12345)     // A source is a new pseudo-random [Source] seeded with the given value.. Same source will output same pseudo-random numbers. Use time.Now().UnixNano() for a varying source
	randomGenerator := rand.New(source) // A random number generator
	println(randomGenerator.Intn(10))
	println(randomGenerator.Intn(10))
	println(randomGenerator.Intn(10)) // always output the same random numbers because the source is the same
}
