package main

import (
	"encoding/json"
	"fmt"
)

type MyStruct struct {
	FirstName string `json:"first_name"`
	Age       int    `json:"age"`
}

func main() {

	jsonData := `{
		"first_name": "Henry",
		"age": 30
	}`

	// into a struct
	data := MyStruct{}
	json.Unmarshal([]byte(jsonData), &data)
	fmt.Printf("%+v", data)

	// into a map
	data2 := make(map[string]interface{}) // the "interface" can be any type
	json.Unmarshal([]byte(jsonData), &data2)
	fmt.Printf("%+v", data2)
}
