package main

// import "fmt" // single import
import (
	"fmt"
	"time"
)

func main() {
	time.Now().UnixNano()
	fmt.Println("Hello World!")
}
