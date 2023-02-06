'''
1. 아이디어
- f(x) = x무게만큼 배낭에 넣을 수 있는 물건들의 가치의 최댓값
- 이중 for 문으로 i 무게의 max 값을 리스트로 담는다.

2. 시간복잡도
- 이중 for문 : O(N^2)

3. 자료구조
- n, k : int
- 물건 무게 items: int[]
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)

for i in range(n):
    for j in range(k, items[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])

print(dp[k])