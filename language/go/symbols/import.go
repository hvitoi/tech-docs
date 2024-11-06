package main

// import "fmt" // single import
import (
	"fmt"
	"time"
	// "github.com/pulumi/pulumi/sdk/v3/go/pulumi" // import from github repo (alias as "pulumi")
	// package_name "my-module/sub_folder" // import the <package_name> contained in any file within the <sub_folder>
	// "my-module/sub_folder" // import from the folder <sub_folder> the package called <sub_folder>
)

func main() {
	time.Now().UnixNano()
	fmt.Println("Hello World!")
}
