package main

import (
	"flag"
	"fmt"
)

func main() {
	nameArg := flag.String("name", "Henry", "just pass a name")
	ageArg := flag.Int("age", 30, "just pass an age")
	flag.Parse()

	fmt.Println(*nameArg)
	fmt.Println(*ageArg)
}