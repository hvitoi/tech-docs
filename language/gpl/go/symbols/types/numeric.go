package main

import "fmt"

func main() {
	// uint (uint8, uint16, uint32, uint64)
	// ...

	// int (int8, int16, int32, int64)
	var myNumber1 int = 4
	mynumber2 := 5
	fmt.Println(myNumber1, mynumber2)

	// float (float32, float64)
	var myFloat float64 = 4.2
	myFloat2 := 4.2
	myFloat3 := float64(1)
	fmt.Println(myFloat, myFloat2, myFloat3)

	// complex (complex64, complex128)
	var myComplex1 complex128 = 0.867 + 0.5i
	myComplex2 := 0.867 + 0.5i
	fmt.Println(myComplex1, myComplex2)

	// byte (alias for uint8)

	// rune (alias for uint32)
}
