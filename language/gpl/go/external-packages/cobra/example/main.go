package main

import (
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/spf13/cobra"
)

func main() {
	var shout bool

	rootCmd := &cobra.Command{
		Use:   "myapp",
		Short: "A tiny example CLI",
	}

	greetCmd := &cobra.Command{
		Use:   "greet [name]",
		Short: "Greet someone",
		Args:  cobra.ExactArgs(1),
		Run: func(cmd *cobra.Command, args []string) {
			msg := "Hello, " + args[0] + "!"
			if shout {
				msg = strings.ToUpper(msg)
			}
			fmt.Println(msg)
		},
	}
	greetCmd.Flags().BoolVarP(&shout, "shout", "s", false, "print in uppercase")

	divideCmd := &cobra.Command{
		Use:   "divide [a] [b]",
		Short: "Divide a by b",
		Args:  cobra.ExactArgs(2),
		// RunE works like Run, except the function returns an error.
		RunE: func(cmd *cobra.Command, args []string) error {
			a, err := strconv.Atoi(args[0])
			if err != nil {
				return err
			}
			b, err := strconv.Atoi(args[1])
			if err != nil {
				return err
			}
			if b == 0 {
				return errors.New("cannot divide by zero")
			}
			fmt.Println(a / b)
			return nil
		},
	}

	rootCmd.AddCommand(greetCmd, divideCmd)

	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
