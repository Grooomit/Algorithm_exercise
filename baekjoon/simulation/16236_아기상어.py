"""
1. 아이디어
- 자신보다 큰 숫자는 지나갈 수 없다.
- 작은 물고기는 먹을 수 있고 지나갈 수 있다.
- 같은 물고기는 먹을 수 없고, 지나갈 수는 있다.

=> BFS 로 자신보다 작은 숫자가 존재하는지 확인
=> 존재한다면 이동 (한칸당 1초)
=> 존재하지 않는다면 종료
=> 여러마리 존재한다면 거리가 가장 가까운 -> 가장 위쪽 -> 가장 왼쪽

2. 시간복잡도
- while : O(V*E) = 20*20 = 400 < 2억 (가능)

3. 자료구조
- 공간 : int[][]
- 상어 크기 : int
- 상어 위치 : int, int
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
y, x, size = 0, 0, 2

for i in range(N):
    for j in range(N):
        if space[j][i] == 9:
            y, x = j, i

def bfs(y, x, size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    temp = []

    while q:
        ey, ex = q.popleft()

        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0:
                if space[ny][nx] <= size:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[ey][ex] + 1
                    
                    if space[ny][nx] < size and space[ny][nx] != 0:
                        temp.append((ny, nx, distance[ny][nx]))

    return sorted(temp, key=lambda x: (-x[2],-x[0],-x[1]))

cnt = 0
result = 0
while 1:
    shark = bfs(y, x, size)

    if len(shark) == 0:
        break

    ny, nx, dist = shark.pop()
    result += dist
    space[y][x], space[ny][nx] = 0, 0

    y, x = ny, nx
    cnt += 1

    if cnt == size:
        size += 1
        cnt = 0

print(result)