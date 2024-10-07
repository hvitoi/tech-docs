package main

import "fmt"

func main() {
	fmt.Println(greeting("Henry"))
}

func greeting(name string) string {
	return "Hello " + name + "!"
}
