package main

import (
	"fmt"
)

var x int
var y float64

func main() {
	// String is made out of slice and bites.
	s := "Hello fuckers"
	fmt.Println(s)

	// Convert from type string to slice and bite.
	bs := []byte(s)
	fmt.Println(bs)
	fmt.Printf("%T\n", s)

	for i := 0; i < len(s); i++ {
		fmt.Printf("%#U", s[i])
	}

	fmt.Println("")

	for i, v := range s {
		fmt.Println(i, v)
	}
}
