package main

func main() {
	letters := []string{"a", "b", "c"}

	// range for with arrays
	for i, letter := range letters {
		println(i, letter)
	}
	for i := range letters { // only the index
		println(i)
	}

	// range for with maps
	info := map[string]string{
		"name":  "Henry",
		"email": "henry@example.com",
	}
	for key, val := range info {
		println(key, val)
	}

	// traditional for
	for i := 0; i < len(letters); i++ {
		println(i, letters[i])
	}

	// infinite loop
	for {
		println("Hello!")
	}

}
