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

# For loop statement


```
package main

import (
	"fmt"
)

func main() {
	x := 1
	for x < 10 {
		//break loop based on condition
		if x > 8 {
			break
		}
		fmt.Println(x)
		// x++ means add 1 eachtiime
		x++
	}
	fmt.Println("done")
}

```

# Loop with multiple if's statement break and continue 


```
package main

import (
	"fmt"
)

func main() {
	x := 0
	if x > 100 {
		break
	}
	if x%2 != 0 {
		continue
	}

	fmt.Println(x)
	// x++ means add 1 eachtiime
	x++
	fmt.Println("done")
}

```




# Linux commands in go and error handling

```
package main

import (
	"fmt"
	"os"
	"os/exec"
)

func execute() {

	// here we perform the pwd command.
	// we can store the output of this in our out variable
	// and catch any errors in err
	out, err := exec.Command("lsdvsdvs").Output()

	// if there is an error with our execution
	// handle it here
	if err != nil {
		fmt.Printf("%s", err)
		fmt.Println(" Error happened")
		os.Exit(1)
	}
	// as the out variable defined above is of type []byte we need to convert
	// this to a string or else we will see garbage printed out in our console
	// this is how we convert it to a string
	fmt.Println("Command Successfully Executed")
	output := string(out[:])
	fmt.Println(output)
}

// This is how you call function on go
func main() {
	execute()
}
```
