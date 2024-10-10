package main

import (
	"fmt"
	"io"
	"net/http"
)

// The defer keyword is used to delay the execution of a function until the surrounding function returns
// In other words, it's like a "cleanup" auxiliary function executed at the very end of at function

func main() {
	resp, _ := http.Get("https://httpbin.org/get")
	defer resp.Body.Close() // Ensures the body is closed at the end of the function (regardless if it program has crashed or exited early)
	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}
