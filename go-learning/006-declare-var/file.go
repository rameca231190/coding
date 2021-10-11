package main

import (
	"fmt"
)

// Use var to declare variable outside of your function.

var y = 43

// Default fo integer is 0.
var z int

func main() {
	// Short declaration operator.
	// Declare variable and ssign a value at the same time (of a certain type).

	x := 42
	fmt.Println(x)
	fmt.Println(y)
	foo()

	fmt.Println(z)
}

func foo() {
	fmt.Println("again:", y)
}
