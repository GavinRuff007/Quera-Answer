package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// توابع هر عملیات
func ShiftRight(s string, n int) string {
	l := len(s)
	if l == 0 {
		return s
	}
	n = n % l
	return s[l-n:] + s[:l-n]
}

func ShiftLeft(s string, n int) string {
	l := len(s)
	if l == 0 {
		return s
	}
	n = n % l
	return s[n:] + s[:n]
}

func Extend(s string, n int) string {
	return s + strings.Repeat("*", n)
}

func Shrink(s string, n int) string {
	l := len(s)
	if n >= l {
		return ""
	}
	return s[:l-n]
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func Put(s string, idx int, c string) string {
	runes := []rune(s)
	if idx-1 < 0 || idx-1 >= len(runes) {
		return s
	}
	runes[idx-1] = []rune(c)[0]
	return string(runes)
}

// تابع اصلی
func main() {
	reader := bufio.NewReader(os.Stdin)
	// خواندن رشته اولیه
	initial, _ := reader.ReadString('\n')
	initial = strings.TrimSpace(initial)

	current := initial

	for {
		line, _ := reader.ReadString('\n')
		line = strings.TrimSpace(line)
		if line == "" {
			continue
		}
		if line == "EXIT" {
			break
		}

		fields := strings.Fields(line)
		cmd := fields[0]

		switch cmd {
		case "SHIFT-R":
			n, _ := strconv.Atoi(fields[1])
			current = ShiftRight(current, n)
		case "SHIFT-L":
			n, _ := strconv.Atoi(fields[1])
			current = ShiftLeft(current, n)
		case "EXTEND":
			n, _ := strconv.Atoi(fields[1])
			current = Extend(current, n)
		case "SHRINK":
			n, _ := strconv.Atoi(fields[1])
			current = Shrink(current, n)
		case "REVERSE":
			current = Reverse(current)
		case "PUT":
			i, _ := strconv.Atoi(fields[1])
			c := fields[2]
			current = Put(current, i, c)
		case "PRINT":
			fmt.Println(current)
		}
	}
}
