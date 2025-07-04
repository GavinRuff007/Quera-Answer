package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func standardize(s string) string {
	var b strings.Builder
	for _, ch := range s {
		if unicode.IsSpace(ch) {
			continue
		}
		b.WriteRune(unicode.ToLower(ch))
	}
	return b.String()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var board []string
	for scanner.Scan() {
		line := scanner.Text()
		board = append(board, line)
	}

	n := len(board)
	m := 0
	for _, line := range board {
		if len(line) > m {
			m = len(line)
		}
	}

	// Find boxes
	type Box struct {
		x1, y1, x2, y2 int
	}
	var boxes []Box

	for i := 0; i < n; i++ {
		for j := 0; j < len(board[i]); j++ {
			if board[i][j] == '+' {
				// try to find a rectangle
				// scan right for + on same row
				for k := j + 1; k < len(board[i]); k++ {
					if board[i][k] == '+' {
						// check if bottom corners exist
						if i+1 < n && k < len(board[i]) {
							for l := i + 1; l < n; l++ {
								if len(board[l]) > j && len(board[l]) > k &&
									board[l][j] == '+' && board[l][k] == '+' {
									// check top and bottom edges are '-' and sides '|'
									valid := true
									for x := j + 1; x < k; x++ {
										if board[i][x] != '-' || board[l][x] != '-' {
											valid = false
											break
										}
									}
									for y := i + 1; y < l; y++ {
										if len(board[y]) <= j || len(board[y]) <= k {
											valid = false
											break
										}
										if board[y][j] != '|' || board[y][k] != '|' {
											valid = false
											break
										}
									}
									if valid {
										boxes = append(boxes, Box{i, j, l, k})
									}
								}
							}
						}
					}
				}
			}
		}
	}

	// for each box, extract course names
	var coursesPerBox [][]string
	for _, box := range boxes {
		var curr []string
		for x := box.x1 + 1; x < box.x2; x++ {
			if box.y1+1 >= len(board[x]) {
				continue
			}
			line := board[x]
			start := box.y1 + 1
			end := box.y2
			if end > len(line) {
				end = len(line)
			}
			course := strings.TrimSpace(line[start:end])
			if course != "" {
				// for safety, each line at most one course name
				curr = append(curr, standardize(course))
			}
		}
		coursesPerBox = append(coursesPerBox, curr)
	}

	// Remove duplicate courses in a box
	for i := range coursesPerBox {
		seen := make(map[string]bool)
		var unique []string
		for _, s := range coursesPerBox[i] {
			if !seen[s] {
				unique = append(unique, s)
				seen[s] = true
			}
		}
		coursesPerBox[i] = unique
	}

	// brute-force all 3-combinations of boxes
	minCourses := 1000000
	b := len(coursesPerBox)
	for i := 0; i < b; i++ {
		for j := i + 1; j < b; j++ {
			for k := j + 1; k < b; k++ {
				all := make(map[string]bool)
				for _, s := range coursesPerBox[i] {
					all[s] = true
				}
				for _, s := range coursesPerBox[j] {
					all[s] = true
				}
				for _, s := range coursesPerBox[k] {
					all[s] = true
				}
				if len(all) < minCourses {
					minCourses = len(all)
				}
			}
		}
	}
	fmt.Println(minCourses)
}
