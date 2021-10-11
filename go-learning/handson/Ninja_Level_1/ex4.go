package main

import (
	"fmt"
)

type nicklson int

var x nicklson

func main() {
	fmt.Println(x)
	fmt.Printf("%T\n", x)
	x = 42
	fmt.Println(x)
}
