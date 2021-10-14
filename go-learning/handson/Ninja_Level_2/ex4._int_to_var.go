// Use operatores and assign their values to variables

package main

import "fmt"

func main() {
	a := 42
	fmt.Printf("%d\t%b\t%#x", a, a, a)

	b := a << 1
	fmt.Printf("%d\t%b\t%#x", b, b, b)

}
