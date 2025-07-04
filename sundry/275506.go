package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	pages := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&pages[i])
	}

	totalPages := 0
	for _, p := range pages {
		// If odd, add a blank page
		if p%2 != 0 {
			p++
		}
		totalPages += p
	}

	// Each A4 sheet holds 2 pages (double-sided)
	sheets := totalPages / 2
	fmt.Println(sheets)
}
