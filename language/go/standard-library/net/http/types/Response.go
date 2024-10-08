package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	resp, _ := http.Get("https://google.com")
	body(resp)
}

func body(resp *http.Response) {
	// The response body data implements the io.ReadCloser interface (Reader + Closer)
	bs := make([]byte, 99999)
	resp.Body.Read(bs) // read the data into the bs
	fmt.Println(string(bs))

	// Alternative with ReadAll
	bodyBinary, _ := io.ReadAll(resp.Body)
	fmt.Println(string(bodyBinary))
}
