package main

import (
	"fmt"
	"net/http"
	"os"
	"sync"
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

// the Closer interface is composed of the Reader and Closer interfaces
func main() {
	// HTTP example
	resp, _ := http.Get("https://httpbin.org/get")
	defer resp.Body.Close() // always close the Closer interfaces

	// File example
	file, _ := os.Open("example.txt")
	defer file.Close() // Ensures file is closed when the function ends

	// Mutex example
	var mu sync.Mutex
	mu.Lock()         // Lock the mutex
	defer mu.Unlock() // Ensure the mutex is unlocked when the function ends

	// Timing execution
	slowFunction()

	// ... panic recover, database connections, etc
}
