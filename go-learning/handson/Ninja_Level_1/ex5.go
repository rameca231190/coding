package main

import (
	"fmt"
)

type nicklson int

var x nicklson
var y int

func main() {
	fmt.Println(x)
	fmt.Printf("%T\n", x)
	x = 42
	fmt.Println(x)
	y = int(y)
	fmt.Printf("%T\n", y)
}
