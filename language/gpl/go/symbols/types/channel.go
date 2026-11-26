package main

func main() {

	// Create channel
	c := make(chan string)
	// c2 := make(chan string, 100) // a buffered channel

	// Create a new go routine to send message to channel
	go SendMessage("a", c)
	go SendMessage("b", c) // waits for the previous msg to be consumed
	go SendMessage("c", c) // waits for the previous msg to be consumed

	// Get message from channel
	println(<-c)
	println(<-c)
	println(<-c) // the order of pickup is not guaranteed
	// println(<-c) // error! Nothing to read

	// close the channel so no other sender can send to it
	close(c)

	// for i := range c {
	// 	fmt.Println(i) // executes until the channel is closed: close(c)
	// }

}

func SendMessage(message string, c chan string) {
	c <- message // The sender waits until channel is empty (all the messages have been consumed). Or if it is a buffered channel.
}
