package main

import (
	"encoding/json"
	"fmt"
)

// An "interface type" is defined as a set of method signatures
// A value of interface type can hold any value that implements those methods.

type bot interface {
	getGreeting() string
	// The interface can also "inherit" other interfaces
}

type number interface {
	int | int8 | int16 | float32 | float64 // ~ same idea of constraints.Ordered
}

// Interfaces are implemented implicitly: a type implements the "bot" interface if implements all the required methods
type englishBot struct{}
type spanishBot struct{}

func (bot englishBot) getGreeting() string {
	return "Hello"
}

func (bot spanishBot) getGreeting() string {
	return "Hola"
}

// Empty interface ("any" is an alias)
type myEmptyInterface interface{}

func main() {
	var eb bot = englishBot{}
	var sb bot = spanishBot{}

	println(eb.getGreeting())
	println(sb.getGreeting())

	// the "interface" can be any type
	data := make(map[string]interface{})
	data2 := make(map[string]any) // "any" is an alias for interface{}

	jsonData := `{
		"first_name": "Henry",
		"colors": ["red", "green", "blue"]
	}`

	json.Unmarshal([]byte(jsonData), &data)

	fmt.Println(data, data2)

	// when the JSON data is unmarshalled, each json data is represented as an interface{}
	// You can assert the interface into a specific type in order to treat the object as its "real" type
	// otherwise go would never know it's a slice
	if colors, ok := data["colors"].([]any); ok {
		fmt.Println("Number of colors:", len(colors))
	} else {
		fmt.Println("Colors is not an array")
	}
}
