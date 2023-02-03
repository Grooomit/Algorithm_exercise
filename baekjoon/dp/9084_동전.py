'''
1. 아이디어
- DP - 동전 경우의 수
- 각 동전으로 k 원을 만들 수 있는 경우의 수 배열을 모두 합한다.

2. 시간복잡도
- 이중 for 문 : O(N^2)

3. 자료구조
- 동전리스트 coins: int[]
- 테스트 케이스의 수: int
- 동전의 갯수 N: int
- 금액 M : int
- 경우의수 list : int[]
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1

    for i in coin:
        for j in range(i, M+1):
            dp[j] += dp[j-i]
    
    print(dp[M])