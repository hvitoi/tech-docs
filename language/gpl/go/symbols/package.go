package main // Package name
// It's the first line of every go file contains the package it belongs to

// There are two types of packages
//  - Executable: Generates a executable binary. The "main package" is the only executable package. The main package must define a "main function", which is the entrypoint
//  - Reusable: Code used as helper with reusable logic. Every other package except "main" is a reusable package

// Multiple files within a project can have the same package name
// Functions defined within the same package can freely call functions defined in other files

import "fmt"

func main() { // Executable package
	fmt.Println("Hello World!")
}
