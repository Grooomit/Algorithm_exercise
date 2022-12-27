"""
1. 아이디어
- while 문으로 현재 방향으로 이동(한칸 이동할 때 +1초) 
    -> 사과가 존재하면 머리만 이동 / 사과가 없다면 꼬리, 머리이동
- 이동하는 방향에 벽이나 몸이 존재한다면 게임 종료, 게임 소요시간 출력

2. 시간복잡도
- while : O(V*M) = 100*100 = 10000 < 1억 (가능)

3. 자료구조
- 시간 : int
- N*N 맵 : int[][]
- 뱀의 머리 : int, int
- 뱀의 꼬리 : deque()
- 뱀의 방향 : int
- 방향 전환 데이터 : dict()
"""
from collections import deque
import sys
input = sys.stdin.readline

direction = dict()
N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 2

L = int(input())
for _ in range(L):
    s, dir = input().split()
    direction[int(s)] = dir

tail = deque()
tail.append((0, 0))
board[0][0] = 1
hy, hx = 0, 0
dir = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
cnt = 0

def turn(num):
    global direction, dir
    if direction.get(cnt) == 'D':
        dir = (dir + 1)%4
    else:
        dir = (dir - 1)%4

while 1:
    cnt += 1
    hy += dy[dir]
    hx += dx[dir]

    if 0<=hy<N and 0<=hx<N and board[hy][hx] != 1:
        if board[hy][hx] == 0:
            y, x = tail.popleft()
            board[y][x] = 0
            
        board[hy][hx] = 1
        tail.append((hy, hx))
        if cnt in direction:
            turn(cnt)
    else:
        break

print(cnt)