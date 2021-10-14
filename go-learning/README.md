## Golang cheet sheet


# Loops in golang

```
package main

import (
	"fmt"
)

func main() {
	// How the loop looks like for init: condition; post
	// i equals to 0 and while i <= 100, ++ increment i value by 1.
	for i := 0; i <= 100; i++ {
		fmt.Println(i)
	}
}

```

# Nesting loops.

```
package main

import (
	"fmt"
)

func main() {
	// i equals to 0 and while i <= 100, ++ increment i value by 1.
	for i := 0; i <= 10; i++ {
		// i < 3 means less then, so it will go from 0,1,2.
		fmt.Printf("The outer loop: %d\n", i)
		for j := 0; j < 3; j++ {
			fmt.Printf("\t\t The inner loop: %d\n", j)
		}
	}
}

```
