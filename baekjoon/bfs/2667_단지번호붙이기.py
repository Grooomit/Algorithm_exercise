# 아이디어 : 이중 for 문으로 map 순회 -> 1의 갯수 하나당 cnt++ 단지수 합산해서 출력
# 시간복잡도 : O(V+E) = (25*25 + 25*25-1) = 625+624 = 1249
# 자료구조 : map = int[][], cnt = int, visited = boolean[][]

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
num = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x):
    q = [(y, x)]
    cnt = 1
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if map[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    num.append(cnt)

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            bfs(j, i)

print(len(num), *sorted(num), sep="\n")