package main

import "fmt"

func main() {
    var n, k int
    fmt.Scan(&n, &k)

    queue := []int{n}
    visited := make([]bool, 100001)
    dist := make([]int, 100001)
    visited[n] = true

    for len(queue) > 0 {
        pos := queue[0]
        queue = queue[1:]

        if pos == k {
            fmt.Println(dist[pos])
            return
        }

        if pos-1 >= 0 && !visited[pos-1] {
            queue = append(queue, pos-1)
            visited[pos-1] = true
            dist[pos-1] = dist[pos] + 1
        }

        if pos+1 <= 100000 && !visited[pos+1] {
            queue = append(queue, pos+1)
            visited[pos+1] = true
            dist[pos+1] = dist[pos] + 1
        }

        if 2*pos <= 100000 && !visited[2*pos] {
            queue = append(queue, 2*pos)
            visited[2*pos] = true
            dist[2*pos] = dist[pos] + 1
        }
    }
}
