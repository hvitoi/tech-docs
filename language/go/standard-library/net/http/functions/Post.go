package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func main() {
	// Request body
	apiURL := "https://httpbin.org/post"
	requestBody, _ := json.Marshal(map[string]string{
		"name":  "Henry",
		"email": "henry@example.com",
	})

	// Send HTTP request
	resp, _ := http.Post(apiURL, "application/json", bytes.NewBuffer(requestBody))
	defer resp.Body.Close() // ensure that reader function (from the response body) is properly closed (even if the function exits early)

	// Read response body
	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("%+v", string(body))
}
