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

	// Initialize struct (by named arguments)
	someone := Person{
		FirstName: "Henry",
		Age:       30,
		Contact: ContactInfo{
			Email:   "a@example.com",
			ZipCode: 94000,
		},
	}

	// Initialize struct (by position arguments)
	someone2 := Person{"Henry", 30, ContactInfo{"a@example.com", 94000}}
	fmt.Printf("%+v\n", someone2)

	// Initialize struct (empty)
	someone3 := Person{}
	fmt.Printf("%+v\n", someone3) // Values are initialized with the Zero values

	// Access struct fields
	fmt.Printf("%v\n", someone.FirstName)

	// Modify struct fields
	someone.FirstName = "Henrique"

	// Manipulating via pointers
	pSomeone := &someone
	pSomeone.FirstName = "Henriquo" // no need to write "*pSomeone.Firstname"

	// Array of structs
	s := []struct {
		x int
		y int
	}{
		{1, 2},
		{3, 4},
	}
	fmt.Printf("%+v", s)
}
