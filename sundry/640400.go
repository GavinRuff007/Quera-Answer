package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Reaction struct {
	needCount int
	inputs    []int
	outputs   []int
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	// خواندن n، نادیده گرفتن m، خواندن k
	line, _ := reader.ReadString('\n')
	parts := strings.Fields(line)
	n, _ := strconv.Atoi(parts[0])
	k, _ := strconv.Atoi(parts[2])

	// خواندن مواد اولیه موجود
	line, _ = reader.ReadString('\n')
	parts = strings.Fields(line)
	have := make([]bool, n+1)
	queue := []int{}
	for _, s := range parts {
		v, _ := strconv.Atoi(s)
		if !have[v] {
			have[v] = true
			queue = append(queue, v)
		}
	}

	// خواندن واکنش‌ها
	reactions := make([]Reaction, k)
	waiting := make([][]int, n+1)

	for i := 0; i < k; i++ {
		// خواندن p و q
		line, _ = reader.ReadString('\n')
		parts = strings.Fields(line)
		p, _ := strconv.Atoi(parts[0])
		q, _ := strconv.Atoi(parts[1])

		// ورودی‌ها
		line, _ = reader.ReadString('\n')
		parts = strings.Fields(line)
		inp := make([]int, p)
		for j := 0; j < p; j++ {
			inp[j], _ = strconv.Atoi(parts[j])
			waiting[inp[j]] = append(waiting[inp[j]], i)
		}

		// خروجی‌ها
		line, _ = reader.ReadString('\n')
		parts = strings.Fields(line)
		out := make([]int, q)
		for j := 0; j < q; j++ {
			out[j], _ = strconv.Atoi(parts[j])
		}

		reactions[i] = Reaction{
			needCount: p,
			inputs:    inp,
			outputs:   out,
		}
	}

	// پردازش BFS برای تولید مواد
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		for _, rid := range waiting[current] {
			reactions[rid].needCount--
			if reactions[rid].needCount == 0 {
				for _, out := range reactions[rid].outputs {
					if !have[out] {
						have[out] = true
						queue = append(queue, out)
					}
				}
			}
		}
	}

	// آماده‌سازی خروجی
	var result []int
	for i := 1; i <= n; i++ {
		if have[i] {
			result = append(result, i)
		}
	}

	// مرتب‌سازی نتیجه
	sort.Ints(result)

	// چاپ خروجی
	fmt.Println(len(result))
	for i, v := range result {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(v)
	}
	fmt.Println()
}
