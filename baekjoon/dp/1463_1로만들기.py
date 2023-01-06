'''
1. 아이디어
- 만약 1이라면 return
- 3, 2 로 나눌 수 있다면 나누고 cnt +1
- 나눌 수 없다면 -1

2. 시간복잡도
- while

3. 자료구조
- 횟수 cnt : int
'''

import sys
input = sys.stdin.readline

N = int(input())
dp = {1: 0, 2: 1}

def make_one(n):
    if n in dp.keys():
        return dp[n]
    
    if n % 6 == 0:
        dp[n] = min(make_one(n//3) + 1, make_one(n//2) + 1)
    elif n % 3 == 0:
        dp[n] = min(make_one(n//3) + 1, make_one(n-1) + 1)
    elif n % 2 == 0:
        dp[n] = min(make_one(n//2) + 1, make_one(n-1) + 1)
    else:
        dp[n] = make_one(n-1) + 1
    
    return dp[n]

print(make_one(N))