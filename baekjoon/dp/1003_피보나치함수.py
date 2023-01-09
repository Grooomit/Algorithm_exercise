'''
1. 아이디어
- 문제 : 재귀로 피보나치 구현 시 0과 1이 몇번 호출되는지 출력하라
- DP로 피보나치 구현
- N 일때 0,1 이 몇번호출되는지 출력하는 함수 구현

0 => 1 0
1 => 0 1
2 => 1 + 0 => 1 0 + 0 1 = 1 1
3 => 2 + 1 => 1 1 + 0 1 = 1 2
4 => 2 + 3 => 1 1 + 1 2 = 2 3

2. 시간복잡도
- 재귀 O(N)?

3. 자료구조
- 0, 1 리스트 : int[]
'''

import sys
input = sys.stdin.readline

def fibonacci(n):
    num = [[1,0],[0,1]]

    for i in range(2,n+1):
        num.append([num[i-1][0] + num[i-2][0], num[i-1][1] + num[i-2][1]])
    
    return num[n]

N = int(input())
for _ in range(N):
    num = fibonacci(int(input()))
    print(*num, sep=' ')