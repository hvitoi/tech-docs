package main

// import "fmt" // single import
import (
	"fmt"
	"time"
	// "github.com/pulumi/pulumi/sdk/v3/go/pulumi" // import from github repo (alias as "pulumi")
)

func main() {
	time.Now().UnixNano()
	fmt.Println("Hello World!")
}
