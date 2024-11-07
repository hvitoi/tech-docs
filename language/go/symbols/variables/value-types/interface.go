package main

// Interfaces are contracts to help us manage types

// It is part of this interface all the types that have the getGreeting function associated with it (defined by the receiver)
// An interface cannot be created a value directly out of it
type bot interface {
	getGreeting() string
	// The interface can also "inherit" other interfaces (e.g., ReadCloser)
}

type number interface {
	int | int8 | int16 | float32 | float64 // ~ same idea of constraints.Ordered
}

// There is no need to specify that english/spanish bots are part of the "bot" interface. It's implicitly inferred because they implement the getGreeting function
type englishBot struct{}
type spanishBot struct{}

func main() {
	eb := englishBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)
}

func (bot englishBot) getGreeting() string {
	return "Hello"
}

func (bot spanishBot) getGreeting() string {
	return "Hola"
}

func printGreeting(b bot) {
	println(b.getGreeting())
}
