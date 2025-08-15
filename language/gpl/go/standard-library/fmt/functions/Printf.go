package main

import "fmt"

type person struct {
	firstName string
	age       int
}

func main() {
	someone := person{"Henry", 30}
	fmt.Printf("%+v", someone)
}
