package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	resp, _ := http.Get("https://httpbin.org/get")
	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}
