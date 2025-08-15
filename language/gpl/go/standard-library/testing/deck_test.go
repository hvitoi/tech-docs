package main

import "testing"

// Test functions carry the same name of the function to be tested with the "Test" prefix
func TestFullDeck(t *testing.T) {
	// "t" is the test handler, which is automatically injected by the testing framework

	aDeck := fullDeck()

	if len(aDeck) != 52 {
		t.Errorf("Deck has incorrect amount of cards")
	}
}
