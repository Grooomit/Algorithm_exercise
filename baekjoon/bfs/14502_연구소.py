'''
1. 아이디어
- 이중 for 문으로 0인 좌표는 리스트에 2인 좌표는 queue에 저장
- 3중 for 문으로 0인 좌표 리스트에서 조합으로 기둥 3개 설치
- 기둥 설치로 만들어진 virus 를 BFS 로 순회
- 감염지역을 제외하고 0의 개수 최댓값을 변수에 저장
- 0 의 갯수가 최대인 값을 리턴

2. 시간복잡도
- 3중 for 문 : O(N^3)
- bfs : O(V+E)

3. 자료구조
- virus : int[][]
- bfs 데이터 처리 : queue
- 0인 좌표 리스트 : list
- cnt 최대 갯수 : int
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]

zero = []
q = deque()

for i in range(M):
    for j in range(N):
        if virus[j][i] == 0:
            zero.append((j, i))
        elif virus[j][i] == 2:
            q.append((j, i))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(arr, queue):

    while queue:
        ny, nx = queue.popleft()
        for k in range(4):
            ey = ny + dy[k]
            ex = nx + dx[k]

            if 0<=ey<N and 0<=ex<M and arr[ey][ex] == 0:
                queue.append((ey, ex))
                arr[ey][ex] = 2

    # 0의 갯수 확인
    return sum(row.count(0) for row in arr)

def make_walls(cnt, start):
    global result

    if cnt == 3:
        copyvirus = [row[:] for row in virus]  # 2차원 리스트 복사
        queue = deque(q)
        result = max(result, bfs(copyvirus, queue))
        return

    for i in range(start, len(zero)):
        y, x = zero[i]
        virus[y][x] = 1
        make_walls(cnt+1, i+1)
        virus[y][x] = 0

result = 0
make_walls(0, 0)
print(result)