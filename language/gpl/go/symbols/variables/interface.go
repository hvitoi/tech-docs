package main

import (
	"encoding/json"
	"fmt"
)

func main() {

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
