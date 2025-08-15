package main

import "fmt"

func main() {

	// Basic assertions
	num := 3
	if num > 0 {
		fmt.Println("Number is positive")
	} else if num < 0 {
		fmt.Println("Number is negative")
	} else {
		fmt.Println("Number is zero")
	}

	// and && or ||
	i := 78
	if i%3 == 0 && i%5 == 0 {
		fmt.Println("FizzBuzz")
	} else if i%3 == 0 {
		fmt.Println("Fizz")
	} else if i%5 == 0 {
		fmt.Println("Buzz")
	} else {
		fmt.Println(i)
	}

	// num is accessible only within the if block
	if foo := 3; foo > 0 {
		fmt.Println("Number is positive")
	} else if foo < 0 {
		fmt.Println("Number is negative")
	} else {
		fmt.Println("Number is zero")
	}

}
