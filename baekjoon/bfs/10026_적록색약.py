'''
1. 아이디어
- BFS. (0,0)부터 BFS 순회
- 현재 상태가 R 또는 G 일때 주변에 R 또는 G 가 있다면 하나의 영역으로 진행
- queue 에 넣고 방문여부 True 로 변경
- BFS 가 한번 진행될때마다 영역 갯수 +1

2. 시간복잡도
- 이중 for문 : O(N^2)

3. 자료구조
- 그림 image : int[][]
- 방문여부 visited : bool[][]
- BFS 큐 queue : deque()
- 현재 색깔 status : string
- 영역 갯수 cnt : int
'''

import sys
input = sys.stdin.readline

N = int(input())
image = (list(input().strip()) for i in range(N))
visited = [[False]* N for i in range(N)]
rg_visited = [[False]* N for i in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def BFS(y, x, c, rg, visit):
    q = [(y, x)]
    visited[y][x] = True

    while q:
        ny, nx = q.pop()
        for k in range(4):
            ey = ny + dy[k]
            ex = nx + dx[k]

            if (ey < 0 or ey > N-1) or (ex < 0 or ex > N-1):
                continue
            if visit[ey][ex]:
                continue
            if image[ey][ex] == c or (rg and (c in "RG" and image[ey][ex] in "RG")):
                q.append((ey, ex))
                visit[ey][ex] = True

cnt, rg_cnt = 0, 0

for i in range(N):
    for j in range(N):
        if not visited[j][i]:
            cnt += 1
            BFS(j, i, image[j][i], False, visited)
        if not rg_visited[j][i]:
            rg_cnt += 1
            BFS(j, i, image[j][i], True, rg_visited)

print(cnt, rg_cnt)