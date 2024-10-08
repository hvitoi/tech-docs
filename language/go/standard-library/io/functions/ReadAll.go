package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	resp, _ := http.Get("https://google.com")
	bodyBinary, _ := io.ReadAll(resp.Body)
	fmt.Println(string(bodyBinary))
}
