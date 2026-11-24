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
	// %v
	fmt.Printf("%v \n", person{"Henry", 30})
	fmt.Printf("%+v \n", person{"Henry", 30}) // more verbose

	// %g (number with decimal spaces)
	fmt.Printf("%g \n", math.Sqrt(7))

	// %T (type of the var)
	fmt.Printf("%T \n", false)

	// %t (the value detailed)
	fmt.Printf("%t \n", 12)

}
