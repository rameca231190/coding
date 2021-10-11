package main

import (
	"fmt"
)

// Use var to declare variable outside of your function.

//Int
var y = 43

//Str
var z = "Shaken, no stirred"

var a string = `James said, "Shaken not stirred"`

func main() {
	fmt.Println(y)
	fmt.Printf("%T\n", y)

	fmt.Println(z)
	fmt.Printf("%T\n", z)

	fmt.Println(a)
	fmt.Printf("%T\n", a)
}
