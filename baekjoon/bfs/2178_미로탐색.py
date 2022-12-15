# 아이디어 : 이중 for 문으로 map 순회 => 1을 지날때마다 (거리 +1), if 현재 방문위치가 (n,m) 이면 종료
# 시간복잡도 : BFS - O(V+E) = 24+23 = 47(?)
# 자료구조 : map = int[][] result = map[n-1][m-1]
from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1, 0, -1, 0] 
dy = [0, 1, 0, -1]

def bfs(y, x):
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()

        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1:
                    map[ny][nx] = map[ey][ex] + 1
                    q.append((ny,nx))
                    
    return map[n-1][m-1]

print(bfs(0,0))