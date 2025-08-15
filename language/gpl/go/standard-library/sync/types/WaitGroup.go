package main

import (
	"fmt"
	"sync"
)

func doSomething() {
	fmt.Println("Do something")
}

func main() {
	go doSomething()
	go doSomething()

	// Wait for goroutines to finish
	var wg sync.WaitGroup
	wg.Add(1)
	wg.Wait()
}
