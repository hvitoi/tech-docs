package main

func main() {
	cards := newDeck()
	cards.shuffle()
	cards.print() // print() can be called because we set up a receiver for the deck type variable
}