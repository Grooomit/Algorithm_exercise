'''
1. 아이디어
- bfs 로 상한 토마토 주변부터 순회 => 익은 토마토를 기준으로 +1 씩 증가
- 만약 주변토마토가 이미 1 이상이면 더 작은 값을 넣기

2. 시간복잡도
- O(V + E) = 1000*1000 + 1000*1000 -1 = 2000000

3. 자료구조
- 토마토가 담긴 상자 box : int[][]
- 큐 q : deque()
'''
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

tomato = deque()
for i in range(M):
    for j in range(N):
        if box[j][i] == 1:
            tomato.append((j, i))

def bfs(q):

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M and box[ny][nx] != -1:
                if box[ny][nx] == 0:
                    box[ny][nx] = box[ey][ex] + 1
                    q.append((ny, nx))

bfs(tomato)

def solution():
    day = 0
    for i in range(M):
        for j in range(N):
            if box[j][i] == 0:
                return -1
            if box[j][i] > day:
                day = box[j][i] - 1
    return day

print(solution())