from collections import deque

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]
# BFS -> 그림 크기 측정
def bfs(y,x):
    rs = 1
    q = deque()
    q = [(y, x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    rs += 1
                    check[ny][nx] = True
                    q.append((ny, nx))
    return rs

cnt = 0
maxs = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            # 전체 그림 갯수를 +1
            cnt += 1
            # BFS -> 그림 크기 측정
            maxs = max(maxs, bfs(j,i))

print(cnt)
print(maxs)