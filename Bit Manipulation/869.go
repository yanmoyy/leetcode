package main

import (
	"slices"
	"strconv"
)

func reorderedPowerOf2(n int) bool {
	sigN := signature(n)
	for i := range 31 {
		if sigN == signature(1<<i) {
			return true
		}
	}
	return false
}

func signature(n int) string {
	digits := []byte(strconv.Itoa(n))
	slices.Sort(digits)
	return string(digits)
}
