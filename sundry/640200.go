package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	const (
		openingLine = "ke ba in dar agar dar bande dar manand, dar manand."
		question    = "dar manand?"
		answer      = "dar manand."
	)

	var n int
	fmt.Scan(&n)

	names := make([]string, n)
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	for i := 0; i < n; {
		if scanner.Scan() {
			line := scanner.Text()
			if line != "" {
				names[i] = line
				i++
			}
		}
	}

	for i := 0; i < n-1; i++ {
		// جمله‌ی اصلی
		fmt.Printf("%s to %s: %s\n", names[i], names[i+1], openingLine)

		// سوال‌ها
		fmt.Printf("%s to %s: %s\n", names[i+1], names[i], question)
		for j := i; j > 0; j-- {
			fmt.Printf("%s to %s: %s\n", names[j], names[j-1], question)
		}

		// پاسخ‌ها
		for j := 0; j <= i; j++ {
			fmt.Printf("%s to %s: %s\n", names[j], names[j+1], answer)
		}
	}
}
