'''
1. 아이디어
- for 문으로 RGB 최솟값을 하나씩 0 ~ N-1 까지 채워나간다.
    - i-1 집의 RGB 중 색이 같지않고 최솟값인 비용을 더한다.
    => rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
- result[N-1] 에서 R G B 중 최솟값을 출력한다.

2. 시간복잡도
- for : O(N)

3. 자료구조
- rgb : int[][]
'''

import sys
input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[N-1]))