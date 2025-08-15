package main

import "fmt"

type ContactInfo struct {
	Email   string
	ZipCode int
}

type Person struct {
	FirstName string `json:"first_name"` // struct tags (useful for encoding/decoding functions)
	Age       int
	Contact   ContactInfo
}

func main() {

	// Initialize Person
	someone := Person{
		FirstName: "Henry",
		Age:       30,
		Contact: ContactInfo{
			Email:   "a@example.com",
			ZipCode: 94000,
		},
	}
	someone.FirstName = "John" // Modify struct
	fmt.Printf("%+v", someone)

	// Alternative way to declare structs
	someone2 := Person{"Henry", 30, ContactInfo{"a@example.com", 94000}}
	fmt.Printf("%+v", someone2)

	// Initialize Person (empty)
	someone3 := Person{}
	fmt.Printf("%+v", someone3)
}
