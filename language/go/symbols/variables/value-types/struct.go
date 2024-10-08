package main

import "fmt"

type contactInfo struct {
	email   string
	zipCode int
}

type person struct {
	firstName string
	age       int
	contact   contactInfo
}

func main() {

	someone := person{
		firstName: "Henry",
		age:       30,
		contact: contactInfo{
			email:   "a@example.com",
			zipCode: 94000,
		},
	}

	someone.firstName = "John" // Modify struct

	fmt.Printf("%+v", someone)

	// Alternative way to declare structs
	someone2 := person{"Henry", 30, contactInfo{"a@example.com", 94000}}
	fmt.Printf("%+v", someone2)

}
