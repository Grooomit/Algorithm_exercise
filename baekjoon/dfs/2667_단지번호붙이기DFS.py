from collections import deque

import sys
input = sys.stdin.readline

m =int(input())
map = [list(map(int, input().strip())) for _ in range(m)]
check = [[False]*m for _ in range(m)]
each = 0
result = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<m and 0<=nx<m:
            if map[ny][nx] == 1 and check[ny][nx] == False:
                check[ny][nx] = True
                dfs(ny, nx)

for j in range(m):
    for i in range(m):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            each = 0
            # DFS 로 크기 구하기
            dfs(j,i)
            # 그림크기를 result 에 추가
            result.append(each)

result.sort()
print(len(result))
print(*result, sep="\n")