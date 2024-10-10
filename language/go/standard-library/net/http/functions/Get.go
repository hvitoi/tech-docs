package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	// Send HTTP request
	apiURL := "https://httpbin.org/get"
	resp, _ := http.Get(apiURL)

	// Read response body
	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("%+v", string(body))
}
