package main

import "fmt"

func main() {
	// All the keys must be of the same type
	// All the values must be of the same type

	colors := map[string]string{
		"red":   "#ff0000",
		"green": "#4bf745",
	}

	// modify map
	colors["white"] = "#ffffff" // create if it does not exist
	// colors.white = "#ffffff" // not possible!

	// delete key
	delete(colors, "green")

	fmt.Println(colors)

	// iterate over a map
	for color, hex := range colors {
		println(color, hex)
	}

}
