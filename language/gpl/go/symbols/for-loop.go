package main

// Components of the for (separated by semicolons):
//   1. init statement
//   2. condition expression
//   3. post statement

func main() {
	letters := []string{"a", "b", "c"}

	// traditional for
	for i := 0; i < len(letters); i++ {
		println(i, letters[i])
	}

	// infinite loop
	// for {
	// 	println("Hello!")
	// }

	// a "while". (omits the init and post statements)
	sum := 1
	for sum < 1000 {
		sum += sum
	}

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

}
