package main

import (
	"strings"
)

func main() {
	letters := []string{"a", "b", "c"}
	joined := strings.Join(letters, ",")
	println(joined)
}
