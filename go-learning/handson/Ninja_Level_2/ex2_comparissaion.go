// Use operatores and assign their values to variables

package main

import "fmt"

func main() {
	a := (42 == 42)
	b := (42 <= 42)
	c := (42 <= 43)
	d := (42 != 43)
	e := (42 < 43)
	f := (42 > 43)
	fmt.Println(a, b, c, d, e, f)
}
