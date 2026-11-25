package main

import (
	"fmt"
	"math"
)

// The "error" interface implements the Error() method

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("I cannot sqrt a negative number: %g", e)
}

func squareRoot(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x)
	}
	return math.Sqrt(x), nil
}

func main() {
	res, err := squareRoot(-4)
	if err != nil {
		fmt.Print(err)
		return
	}
	fmt.Print(res)
}
