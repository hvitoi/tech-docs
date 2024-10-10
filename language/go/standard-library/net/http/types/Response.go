package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	resp, _ := http.Get("https://httpbin.org/get")
	Body(resp)
}

func Body(resp *http.Response) {
	// Read response body
	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))

	// The response body data implements the io.ReadCloser interface (Reader + Closer)
	bs := make([]byte, 99999)
	resp.Body.Read(bs) // read the data into the bs
	fmt.Println(string(bs))
}
