package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	client := &http.Client{}
	do(client)
}

func do(client *http.Client) {
	// Build request
	req, _ := http.NewRequest("GET", "https://httpbin.org/get", nil)

	// Send HTTP request
	resp, _ := client.Do(req)

	// Read response body
	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("%+v", string(body))
}
