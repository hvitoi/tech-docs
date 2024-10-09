package main

import (
	"fmt"
	"net/http"
	"time"
)

// The main function starts the "main go routine"
func main() {
	links := []string{
		"https://google.com",
		"https://facebook.com",
		"https://amazon.com",
		"https://apple.com",
	}

	// It's necessary a channel so that the go routines can communication with the main routine
	c := make(chan string)

	// Create the initial go routines for each link checker
	for _, link := range links {
		// the go keyword can only be used in front of function calls
		go checkLink(link, c)
	}

	// Loop through indefinitely waiting for messages in the channel. Same as "for { fmt.Println(<-c) }"
	for link := range c {
		// the invoked go routine must be "self-contained". The go function cannot receive args from the outer scope. That's why the link has to be passed as parameter
		go func(link string) {
			time.Sleep(5 * time.Second)
			checkLink(link, c)
		}(link)
	}

}

func checkLink(link string, c chan string) {
	_, err := http.Get(link)

	if err == nil {
		fmt.Println(link, "is up!")
	} else {
		fmt.Println(link, "might be down!")
	}

	c <- link // send message into the channel
}
