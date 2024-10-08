package main

import (
	"fmt"
	"strings"
)

func main() {
	letters := "a,b,c"
	split := strings.Split(letters, ",")
	fmt.Println(split)
}
