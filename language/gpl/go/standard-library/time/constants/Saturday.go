package main

import (
	"fmt"
	"time"
)

func main() {
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
}
