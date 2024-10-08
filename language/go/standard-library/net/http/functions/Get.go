package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	// The response is a http.Response struct
	resp, err := http.Get("https://google.com")

	if err != nil {
		os.Exit(1)
	}
	fmt.Printf("%+v", resp)
}
