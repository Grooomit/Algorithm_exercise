"""
1. 아이디어
- A 는 오름차순, B 는 내림차순으로 정렬
- for 문으로 A[index] * B[index] 연산을 한다.

2. 시간복잡도
- for : O(N)

3. 자료구조
- A배열 : int[]
- B배열 : int[]
- 연산결과 cnt : int
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

A.sort()
B.sort(reverse=True)

for i in range(N):
    cnt += A[i] * B[i]

print(cnt)