package main

import (
	"fmt"
	"math"
)

func main() {
	var t float64
	var w int
	fmt.Scan(&t, &w)

	denominator := 2 * (1 - 1/math.Pow(2, float64(w)))
	x := t / denominator

	fmt.Printf("%.4f\n", x)
}
