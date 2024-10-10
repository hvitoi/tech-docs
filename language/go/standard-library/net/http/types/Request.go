package main

import (
	"fmt"
	"net/http"
)

func main() {
	req, _ := http.NewRequest("GET", "https://httpbin.org/get", nil)
	Header(req)
}

func Header(req *http.Request) {
	req.Header.Set("Content-Type", "application/json")
	fmt.Printf("%+v", req)
}
