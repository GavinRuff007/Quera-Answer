package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)

	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	fields := strings.Fields(line)

	a := make([]int, n)
	negCount := 0

	for i := 0; i < n; i++ {
		a[i], _ = strconv.Atoi(fields[i])
		if a[i] < 0 {
			negCount++
		}
	}

	ans := 0
	for i := 0; i < n; i++ {
		if a[i] < 0 {
			ans += negCount - 1
		} else {
			ans += negCount
		}
	}

	fmt.Println(ans)
}
