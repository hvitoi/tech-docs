package main

import "fmt"

// Create a new type (a slice of string)
// the new type extends all the behaviors of slice of strings
// The type itself can be used to cast other types. E.g., deck([]string{"a", "b", "c"})
type deck []string

func fullDeck() deck {
	cards := deck{}

	cardSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	cardValues := []string{"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"}

	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, value+" of "+suit)
		}
	}

	return cards
}

func main() {
	fmt.Println(fullDeck())
}
