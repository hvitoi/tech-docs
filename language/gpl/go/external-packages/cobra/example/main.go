package main

import (
	"fmt"
	"os"
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

	rootCmd.AddCommand(greetCmd)

	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}
