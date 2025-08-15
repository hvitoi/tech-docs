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

	// Build request
	req, _ := http.NewRequest("POST", apiURL, bytes.NewBuffer(requestBody))
	req.Header.Set("Content-Type", "application/json")

	// Send HTTP request
	client := &http.Client{}
	resp, _ := client.Do(req)
	defer resp.Body.Close()

	// Read the response body
	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("%+v", string(body))
}
