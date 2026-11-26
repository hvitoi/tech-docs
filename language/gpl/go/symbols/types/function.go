package main

import (
	"math"
)

func main() {

	// Inline function declaration
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	println(hypot(3, 4))

}
