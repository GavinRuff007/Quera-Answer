package main

import (
	"fmt"
)

func main() {
	var p, q int
	fmt.Scan(&p)
	fmt.Scan(&q)

	if p <= 50 && q <= 10 {
		fmt.Println("White")
	} else if q > 30 {
		fmt.Println("Red")
	} else {
		fmt.Println("Yellow")
	}
}
