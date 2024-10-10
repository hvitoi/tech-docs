package main

import (
	"fmt"
	"time"
)

func trackTime(start time.Time) {
	elapsed := time.Since(start)
	fmt.Printf("Execution took %s\n", elapsed)
}

func slowFunction() {
	defer trackTime(time.Now()) // Measure the time of slowFunction
	time.Sleep(2 * time.Second) // Simulate a slow operation
}

func main() {
	slowFunction()
}
