package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var wr = bufio.NewWriter(os.Stdout)

func scanInt() int {
	sc.Scan()
	text := sc.Text()
	v, _ := strconv.Atoi(text)
	return v
}

func main() {
	defer wr.Flush()
	sc.Split(bufio.ScanWords)

	n := scanInt()
	a, b := make([]int, n), make([]int, n)

	for i := range a {
		a[i] = scanInt()
	}
	for i := range b {
		b[i] = scanInt()
	}

	sort.Ints(a)
	sort.Ints(b)
	sort.Sort(sort.Reverse(sort.IntSlice(b)))

	sum := 0
	for i, value := range a {
		sum += value * b[i]
	}
	fmt.Fprintln(wr, sum)
}
