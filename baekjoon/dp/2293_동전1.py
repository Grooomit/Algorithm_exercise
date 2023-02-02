'''
1. 아이디어
- 중복있음, 순서 상관없음 (조합?)
- f(x) = 동전의 합이 x원이 되도록하는 경우의 수

2. 시간복잡도
- dp

3. 자료구조
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in coins: # i = 1, 2, 5
    for j in range(i, k+1): # i ~ k 까지 
        if j-i >= 0: # 
            dp[j] += dp[j-i]

print(dp[k])