package main

import "fmt"

type UserStore interface {
	GetName(id int) (string, error)
}

type Greeter struct {
	store UserStore
}

func (g Greeter) Greet(id int) (string, error) {
	name, err := g.store.GetName(id)
	if err != nil {
		return "", fmt.Errorf("greet user %d: %w", id, err)
	}
	return "Hello, " + name + "!", nil
}

func main() {}
