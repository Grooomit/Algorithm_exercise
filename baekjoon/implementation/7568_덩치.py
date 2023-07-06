'''
1. 아이디어
- 2차원 리스트를 순회하면서 값 비교
- 나보다 덩치 큰사람이 존재하면 등수 +1

2. 시간복잡도
- 2중 for문 : O(N^2)

3. 자료구조
- 키, 몸무게 리스트 : int[][]
- 등수 rank : int
'''

import sys
input = sys.stdin.readline

N = int(input())
sizes = [list(map(int, input().split())) for _ in range(N)]
result = [0] * N

for i in range(N):
    rank = 1
    for j in range(N):
        if sizes[j][0] > sizes[i][0] and sizes[j][1] > sizes[i][1]:
            rank += 1
    result[i] = rank

print(*result, sep=" ")