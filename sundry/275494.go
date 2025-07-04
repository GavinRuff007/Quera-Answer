package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	var price int
	fmt.Scan(&price)

	for i := 1; i < n; i++ {
		var change int
		fmt.Scan(&change)
		price += change
	}

	fmt.Println(price)
}
