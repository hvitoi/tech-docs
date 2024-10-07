package main // same package as main.go (they now share the functions)

import (
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"strings"
	"time"
)

// Create a new type called 'deck' which is a slice of strings
type deck []string // the new deck type extends all the behavior of slice of strings

func newDeck() deck {
	cards := deck{} // string slice

	cardSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"} // Naipes
	cardValues := []string{"Ace", "Two", "Three", "Four"} // Valores

	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, value + " of " + suit) // append a new item to the slice
		}
	}

	return cards
}

/* CONVENTIONAL FUNCTIONS */

// Split the deck into 2. One with the hand cards, other with the rest
func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

/* RECEIVER FUNCTIONS */

// Iterate over each card of the deck and print
func (d deck) print() {
	for i, card := range d {
		fmt.Println(i, card)
	}
}

// Convert the deck into a comma-separated string
func (d deck) toString() string {
	return strings.Join([]string(d), ",") // convert the deck array into string array and join
}

// Save the deck into a file
func (d deck) saveToFile(filename string) error {
	return ioutil.WriteFile(filename, []byte(d.toString()), 0666)
}

func newDeckFromFile(filename string) deck {
	bs, err := ioutil.ReadFile(filename)
	if err != nil {
		// Option #1 - log the error and return a call to newDeck()
		// Option #2 - Log the error and entirely quit the program
		fmt.Println("Error:", err)
		os.Exit(1)
	}

	s := strings.Split(string(bs), ",")
	return deck(s)
}

func (d deck) shuffle() {
	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)

	for i := range d {
		newPosition := r.Intn(len(d) - 1)

		d[i], d[newPosition] = d[newPosition], d[i]
	}
}
