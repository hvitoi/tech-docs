package main

import (
	"fmt"
	"math"
)

type person struct {
	firstName string
	age       int
}

func main() {
	// struct
	someone := person{"Henry", 30}
	fmt.Printf("%+v \n", someone)

	// number
	fmt.Printf("Square root of 7: %g \n", math.Sqrt(7))

	mybool := false
	fmt.Printf("Type: %T Value: %v\n", mybool, mybool)
}
