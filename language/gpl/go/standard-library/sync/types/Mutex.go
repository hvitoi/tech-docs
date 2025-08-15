package main

import (
	"fmt"
	"sync"
)

var mu sync.Mutex

// mu := sync.Mutex{} // if inside of a function

func criticalSection() {
	mu.Lock()         // Lock the mutex
	defer mu.Unlock() // Ensure the mutex is unlocked when the function ends

	// Critical section of code
	fmt.Println("Critical section")
}

func main() {
	go criticalSection()
	go criticalSection()

	// Wait for goroutines to finish
	var wg sync.WaitGroup
	wg.Add(1)
	wg.Wait()
}
