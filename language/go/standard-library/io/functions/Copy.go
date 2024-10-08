package main

import (
	"io"
	"net/http"
	"os"
)

func main() {
	resp, _ := http.Get("https://google.com")
	io.Copy(os.Stdout, resp.Body) // copy the body to stdout
}
