package main

import "fmt"

// return 1 value
func greeting(name string) string {
	return "Hello " + name + "!"
}

// return multiple values
func userInfo(name string, age int) (string, int) {
	// the return are 2 independent values (not a tuple data type)
	return name, age
}

func main() {
	greetingMessage := greeting("Henry")
	fmt.Println(greetingMessage)

	userName, userAge := userInfo("Henry", 30)
	fmt.Println(userName)
	fmt.Println(userAge)
}
