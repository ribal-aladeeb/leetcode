package main

import "fmt"

var pln = fmt.Println

func main() {
	f := "hey"
	pln(longestPalindrome(f))

}

// func longestPalindrome(s string) string {
// 	if len(s)%2 == 1 {
// 		return oddString(s, len(s)/2)
// 	}
// 	return evenString(s, len(s)/2)
// }

// var largest = make([]int, 0)

// // func oddString(odd string, midpoint int) string {
// // 	bound := 0
// // 	if midpoint < len(odd)-1-midpoint {
// // 		bound = midpoint
// // 	} else {
// // 		bound = len(odd) - 1 - midpoint
// //     }
// //     for
// // }

// // func evenString(even string, lower int) string {
// // 	return ""

// // }
