"""
1. 아이디어
- 특정 조건 만족하는 한 계속 이동 -> While
- for 문으로 4방향 탐색
- 더이상 탐색 안될 경우, 뒤로 한칸 후진
- 후진이 불가능하면 종료

2. 시간복잡도
- While 문 최대 : O(N x M) = 50^2 = 2500 < 2억
- 각 칸에서 4방향 연산 수행 => O(4NM)

3. 자료구조
- 전체지도 : int[][]
- 내 위치, 방향 : (int, int), int
- 청소 횟수 : int
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y,x,d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
# 방향 벡터
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while 1:
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1,5):
        ny = y + dy[d-i]
        nx = x + dx[d-i]

        if 0<=ny<n and 0<=nx<m:
            if map[ny][nx] == 0:
                # 그 방향으로 회전한 다음 한 칸 전진하고 1번부터 진행
                d = (d-i+4) % 4
                y, x= ny, nx
                sw = True
                break

    # 4방향 모두 있지 않은 경우
    if sw == False:
        # 후진이 가능한지 확인
        ny = y - dy[d]
        nx = x - dx[d]

        if 0<=ny<n and 0<=nx<m:
            if map[ny][nx] == 1:
                break
            else:
                y, x = ny, nx
        else:
            break
   
print(cnt)