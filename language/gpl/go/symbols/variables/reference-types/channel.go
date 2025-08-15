package main

func main() {

	// Create channel
	c := make(chan string)

	// Create a new go routine to send message to channel
	go SendMessage("Hello!", c)

	// Get message from channel
	println(<-c)
}

func SendMessage(message string, c chan string) {
	c <- message
}
