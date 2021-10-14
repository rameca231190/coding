// Program that prints a number in decimal, binary and hex

package main

import (
	"fmt"
)

func main() {
	a := 42
	// Print with different formats
	fmt.Printf("%d\t%b\t%#x", a, a, a)
}
