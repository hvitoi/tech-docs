package main

import (
	"fmt"
	"path/filepath"
)

func main() {
	foo := filepath.Join("..", "mypath")
	fmt.Println(foo)
}
