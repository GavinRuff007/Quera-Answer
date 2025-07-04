package main

import (
	"bufio"
	"fmt"
	"os"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var r, c int
	fmt.Scan(&r, &c)
	grid := make([][]byte, r)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; i < r; i++ {
		for {
			scanner.Scan()
			line := scanner.Text()
			if len(line) == c {
				grid[i] = []byte(line)
				break
			}
		}
	}
	// تعداد بچه‌ها
	var ns, nn, nt int
	fmt.Scan(&ns, &nn, &nt)

	// نوع‌ها: 0=empty, 1=short(s), 2=normal(n), 3=tall(t)
	gridType := make([][]int, r)
	for i := 0; i < r; i++ {
		gridType[i] = make([]int, c)
		for j := 0; j < c; j++ {
			switch grid[i][j] {
			case '#':
				gridType[i][j] = 0
			case 's':
				gridType[i][j] = 1
			case 'n':
				gridType[i][j] = 2
			case 't':
				gridType[i][j] = 3
			}
		}
	}

	// در هر ستون، برای هر ردیف بیشترین قد مجاز (1,2,3) را محاسبه کن
	maxAllow := make([][]int, r)
	for i := 0; i < r; i++ {
		maxAllow[i] = make([]int, c)
		for j := 0; j < c; j++ {
			maxAllow[i][j] = 3 // پیش‌فرض همه نوع مجاز
		}
	}
	for col := 0; col < c; col++ {
		maxType := 3
		for row := r - 1; row >= 0; row-- {
			switch gridType[row][col] {
			case 1: // s
				maxType = min(maxType, 1)
			case 2: // n
				maxType = min(maxType, 2)
			case 3: // t
				maxType = min(maxType, 3)
			}
			maxAllow[row][col] = maxType
		}
	}

	// حالا بچه‌ها را حریصانه بچین
	remS, remN, remT := ns, nn, nt
	res := make([][]byte, r)
	for i := 0; i < r; i++ {
		res[i] = make([]byte, c)
		copy(res[i], grid[i])
	}

	for col := 0; col < c; col++ {
		for row := r - 1; row >= 0; row-- {
			if grid[row][col] != '#' {
				continue
			}
			// اینجا می‌توانیم چه کسی بگذاریم؟
			if maxAllow[row][col] >= 3 && remT > 0 {
				res[row][col] = 't'
				remT--
			} else if maxAllow[row][col] >= 2 && remN > 0 {
				res[row][col] = 'n'
				remN--
			} else if maxAllow[row][col] >= 1 && remS > 0 {
				res[row][col] = 's'
				remS--
			} else {
				res[row][col] = '#'
			}
		}
	}

	// چک کن بچه‌ها همه نشسته‌اند یا نه
	if remS > 0 || remN > 0 || remT > 0 {
		fmt.Println("Let's go to the park")
		return
	}

	// چک کن کسی جلوش بلندتر از خودش نباشه
	for col := 0; col < c; col++ {
		frontType := 0
		for row := r - 1; row >= 0; row-- {
			switch res[row][col] {
			case 's':
				if frontType > 1 {
					fmt.Println("Let's go to the park")
					return
				}
				frontType = 1
			case 'n':
				if frontType > 2 {
					fmt.Println("Let's go to the park")
					return
				}
				frontType = 2
			case 't':
				if frontType > 3 {
					fmt.Println("Let's go to the park")
					return
				}
				frontType = 3
			}
		}
	}

	// چاپ جدول نهایی
	for i := 0; i < r; i++ {
		fmt.Println(string(res[i]))
	}
}
