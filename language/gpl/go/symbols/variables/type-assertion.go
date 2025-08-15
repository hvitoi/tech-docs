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

	if colors, ok := data["colors"].([]interface{}); ok {
		fmt.Println("Number of colors:", len(colors))
	} else {
		fmt.Println("Colors is not an array")
	}

	// assert to array and then to string
	favoriteColor := data["colors"].([]interface{})[0].(string)
	fmt.Println(favoriteColor)

}
