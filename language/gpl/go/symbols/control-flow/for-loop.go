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

	// a "while". (omits the init and post statements)
	sum := 1
	for sum < 1000 {
		sum += sum
	}

	// infinite loop (omits all the statements)
	// for {
	// 	println("Hello!")
	// }

	// range for with arrays/slices
	for i, v := range letters {
		println(i, v)
	}
	for i := range letters { // only the index
		println(i)
	}
	for _, v := range letters { // only the val
		println(v)
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
