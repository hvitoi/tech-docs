package main

import (
	"encoding/json"
	"fmt"
)

type MyStruct struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
}

func main() {

	jsonData := `{
		"first_name": "Henry",
		"last_name": "Vitoi"
	}`

	// into a struct
	data := MyStruct{}
	json.Unmarshal([]byte(jsonData), &data)
	fmt.Printf("%+v", data)

	// into a map
	data2 := map[string]string{}
	json.Unmarshal([]byte(jsonData), &data2)
	fmt.Printf("%+v", data2)
}
