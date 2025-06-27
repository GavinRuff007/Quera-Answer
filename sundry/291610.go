package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func normalizePhone(s string) string {
	s = strings.TrimSpace(s)

	if strings.Count(s, "+") > 1 || (strings.Contains(s, "+") && !strings.HasPrefix(s, "+")) {
		return "invalid"
	}

	for i, r := range s {
		if i == 0 && r == '+' {
			continue
		}
		if !unicode.IsDigit(r) {
			return "invalid"
		}
	}

	if strings.HasPrefix(s, "09") && len(s) == 11 {
		return "+98" + s[1:]
	} else if strings.HasPrefix(s, "98") && len(s) == 12 {
		return "+" + s
	} else if strings.HasPrefix(s, "+98") && len(s) == 13 {
		return s
	}

	return "invalid"
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var n int
	fmt.Sscanf(scanner.Text(), "%d", &n)

	for i := 0; i < n; i++ {
		scanner.Scan()
		input := scanner.Text()
		fmt.Println(normalizePhone(input))
	}
}
