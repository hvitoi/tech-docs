package main

func main() {
	// creates an empty reference
	// only works with slice, map or channel

	colors := make(map[string]string)
	// var colors map[string]string // same!

	println(colors)

	// an empty byte slice of size 99999
	bs := make([]byte, 99999)
	println(bs)

}
