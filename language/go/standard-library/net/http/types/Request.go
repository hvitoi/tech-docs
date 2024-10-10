package main

import (
	"fmt"
	"net/http"
)

func main() {
	req, _ := http.NewRequest("GET", "https://httpbin.org/get", nil)
	header(req)
}

func header(req *http.Request) {
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer asdf")
	fmt.Printf("%+v", req)
}
