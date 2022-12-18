'''
1. 아이디어
- dfs => 재귀
- 이중 for 문으로 map 순회 -> 재귀로 붙어있는 배추를 돌면서 방문 True 로 수정 and cnt+=1

2. 시간복잡도
- O(V+E) = 2500+2500 = 5000

3. 자료구조
- map = int[][]
- visited = int[][]
- cnt = int
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    visited[y][x] = True
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<m and 0<=nx<n:
            if arr[ny][nx] == 1 and visited[ny][nx] == False:
                dfs(ny,nx)

N = int(input())
for _ in range(N):
    n, m, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    for j in range(m):
        for i in range(n):
            if arr[j][i] == 1 and visited[j][i] == False:
                dfs(j,i)
                cnt += 1
    print(cnt)