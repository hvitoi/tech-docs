package main

import (
	"fmt"
	"runtime"
	"time"
)

// Evaluation is performed from top to bottom
// The values involved don't need to be constants

func main() {
	day := 3
	switch day {
	case 1:
		println("Monday")
	case 2:
		println("Tuesday")
	case 3:
		println("Wednesday")
	case 4:
		println("Thursday")
	case 5:
		println("Friday")
	case 6:
		println("Saturday")
	case 7:
		println("Sunday")
	default:
		println("Invalid day")
	}

	// With short statement
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("macOS")
	case "linux":
		fmt.Println("Linux")
	default:
		// freebsd, openbsd, etc
		fmt.Printf("%s", os)
	}

	// Non-constant values (even a function can be called in the case statement)
	saturday := time.Saturday
	switch today := time.Now().Weekday(); today { // Saturday = 6
	case saturday - 0:
		fmt.Println("Today is Saturday")
	case saturday - 1:
		fmt.Println("Tomorrow is Saturday")
	case saturday - 2:
		fmt.Println("Saturday is in two days")
	default:
		fmt.Println("Saturday is too far away")
	}

	// Switch without a condition (this will stop to compare to the case output, and instead evaluate the case statement)
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}

	// Type switch
	var i interface{} = 21
	switch v := i.(type) {
	case int:
		fmt.Printf("Twice %v is %v\n", v, v*2)
	case string:
		fmt.Printf("%q is %v bytes long\n", v, len(v))
	default:
		fmt.Printf("I don't know about type %T!\n", v)
	}
}
