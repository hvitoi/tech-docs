package main

import (
	"encoding/json"
	"fmt"
)

type RequestBody struct {
	FirstName string `json:"first_name"` // this tag tells the json functions how to serialize the keys
	LastName  string `json:"last_name"`
}

func main() {

	jsonBody, _ := json.Marshal(RequestBody{
		FirstName: "Henry",
		LastName:  "Vitoi",
	})
	fmt.Println(string(jsonBody))

	jsonBody2, _ := json.Marshal(map[string]string{
		"name":  "Henry",
		"email": "henry@example.com",
	})
	fmt.Println(string(jsonBody2))

}
