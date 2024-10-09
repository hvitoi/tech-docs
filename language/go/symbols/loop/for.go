package main

func main() {
	letters := []string{"a", "b", "c"}

	// range for
	for i, letter := range letters {
		println(i, letter)
	}
	for i := range letters { // only the index
		println(i)
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
