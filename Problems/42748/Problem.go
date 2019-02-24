package main

import "fmt"
import "sort"

func solution(array []int, commands [][]int) []int {
	var answer []int

	for _, command := range commands {
		tmp := make([]int, len(array))
		copy(tmp, array)
		sub := tmp[command[0]-1 : command[1]]
		//fmt.Printf("%v", sub)
		sort.Ints(sub)
		answer = append(answer, sub[command[2]-1])
	}

	return answer
}

func main() {
	fmt.Printf("%v", solution([]int{1, 5, 2, 6, 3, 7, 4}, [][]int{{2, 5, 3}, {4, 4, 1}, {1, 7, 3}}))
}
