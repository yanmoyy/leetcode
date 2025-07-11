package main

func findKDistantIndices(nums []int, key int, k int) []int {
	keyIdxs := []int{}
	for i, num := range nums {
		if num == key {
			keyIdxs = append(keyIdxs, i)
		}
	}
	if len(keyIdxs) == 0 {
		return keyIdxs
	}
	isKdist := make([]bool, len(nums))
	cur := 0
	for i := range nums {
		dist := i - keyIdxs[cur]
		if dist < 0 {
			dist = -dist
		}
		if dist <= k {
			isKdist[i] = true
		}
		if keyIdxs[cur]+k <= i && cur < len(keyIdxs)-1 {
			cur++
		}
	}
	answer := []int{}
	for i, ok := range isKdist {
		if ok {
			answer = append(answer, i)
		}
	}
	return answer
}
