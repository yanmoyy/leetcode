package main

// Get number of odd & even
func flowerGame(n int, m int) int64 {
	oddN, oddM := countOdd(n), countOdd(m)
	return int64(oddN*(m-oddM) + (n-oddN)*oddM)
}

func countOdd(n int) int {
	return n/2 + n%2
}
