package main

import (
	"fmt"
)

func main() {

	data := map[string]interface{}{
		"colors": []interface{}{
			"red",
			"green",
			"blue",
		},
	}

	// You can assert the interface into a specific type in order to treat the object as its "real" type
	// otherwise go would never know it's a slice

	// Assert that the "colors" object is an array of any type (interface{})
	if colors, ok := data["colors"].([]any); ok {
		fmt.Println("Number of colors:", len(colors))
	} else {
		fmt.Println("Colors is not an array")
	}

	// Assertions
	favoriteColor := data["colors"].([]any)[0].(string) // it's an array and first element is a string
	favoriteColor2 := data["colors"].([]string)         // it's an array of strings
	fmt.Println(favoriteColor, favoriteColor2)

}
