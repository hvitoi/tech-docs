package main

import "fmt"

// All the keys must be of the same type
// All the values must be of the same type

func main() {

	colors := map[string]string{
		"red":   "#ff0000",
		"green": "#4bf745",
	}

	// modify map
	colors["white"] = "#ffffff" // create if it does not exist
	// colors.white = "#ffffff" // not possible!

	// delete key
	delete(colors, "green")

	// test if a key exist
	v, ok := colors["green"] // not present anymore
	fmt.Println("The value:", v, "Present?", ok)

	// iterate over a map
	for k, v := range colors {
		println(k, v)
	}

	type IPAddr [4]byte
	hosts := map[string]IPAddr{
		"loopback":  {127, 0, 0, 1}, // no need to instantiate like IPAddr{127, 0, 0, 1}
		"googleDNS": {8, 8, 8, 8},
	}
	fmt.Println(hosts)

}
