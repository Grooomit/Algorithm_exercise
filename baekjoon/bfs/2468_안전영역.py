import sys
input = sys.stdin.readline

N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, h):
    q = [(y, x)]
    visited[y][x] = True

    while q:
        ny, nx = q.pop()
        for k in range(4):
            ey = ny + dy[k]
            ex = nx + dx[k]

            if 0<=ey<N and 0<=ex<N and visited[ey][ex] == False:
                if region[ey][ex] > h:
                    visited[ey][ex] = True
                    q.append((ey, ex))

cnt = 0

# 물의 높이 변경
for h in range(101):
    visited = [[False] * N for _ in range(N)]
    safe_zone = 0
    for i in range(N):
        for j in range(N):
            if visited[j][i] == False and region[j][i] > h:
                bfs(j, i, h)
                safe_zone += 1
    cnt = max(cnt, safe_zone)

print(cnt)