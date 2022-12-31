"""
1. 아이디어
- for 문을 돌면서 큰 금액의 동전부터 차감
- K 를 동전 금액으로 나눈뒤 남은값으로 갱신

2. 시간복잡도
- for : O(N)

3. 자료구조
- 동전 금액 : int[]
    => 1e6 > int 로 가능
- 현재 남은 금액 : int
    => 1e8 > int 로 가능
- 동전 개수 : int
    => 1e8 > int 로 가능
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [ int(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += K // each_coin
    K = K % each_coin

print(cnt)