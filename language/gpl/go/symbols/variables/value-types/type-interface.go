package main

import (
	"encoding/json"
	"fmt"
)

// Interfaces are contracts to help us manage types

// It is part of this interface all the types that have the getGreeting function associated with it (defined by the receiver)
// An interface cannot be created a value directly out of it
type bot interface {
	getGreeting() string
	// The interface can also "inherit" other interfaces (e.g., ReadCloser)
}

type number interface {
	int | int8 | int16 | float32 | float64 // ~ same idea of constraints.Ordered
}

// There is no need to specify that english/spanish bots are part of the "bot" interface. It's implicitly inferred because they implement the getGreeting function
type englishBot struct{}
type spanishBot struct{}

func (bot englishBot) getGreeting() string {
	return "Hello"
}

func (bot spanishBot) getGreeting() string {
	return "Hola"
}

func printGreeting(b bot) {
	println(b.getGreeting())
}

func main() {
	eb := englishBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)

	// the "interface" can be any type
	data := make(map[string]interface{})

	jsonData := `{
		"first_name": "Henry",
		"colors": ["red", "green", "blue"]
	}`

	json.Unmarshal([]byte(jsonData), &data)

	fmt.Println(data)

	// when the JSON data is unmarshalled, each json data is represented as an interface{}
	// You can assert the interface into a specific type in order to treat the object as its "real" type
	// otherwise go would never know it's a slice
	if colors, ok := data["colors"].([]interface{}); ok {
		fmt.Println("Number of colors:", len(colors))
	} else {
		fmt.Println("Colors is not an array")
	}
}
