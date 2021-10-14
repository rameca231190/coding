# How to use multiple comments in one block.

```
package main

import "fmt"

func main() {
	a := `here is something
	as
	a
	raw
	string
	literal
	"you see"
	another thing`
	fmt.Println(a)
}
```

# Iota with constance

Value of iota will start from:
0
1
2
3

```
package main

import "fmt"

const (
	a = 2017 + iota
	b = 2017 + iota
	c = 2017 + iota
	d = 2017 + iota
)

func main() {
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
}
```