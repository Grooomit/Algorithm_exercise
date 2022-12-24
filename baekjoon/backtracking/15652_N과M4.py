"""
1. 아이디어
- 자연수 1~N, 길이 M, 중복가능, 비내림차순
- 백트래킹 재귀함수에서 for 문으로 숫자 선택 (for i in range(num, n+1))

2. 시간복잡도
- N! <= 8 (가능)

3. 자료구조
- 결과 int[]

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []

def dfs(num):
    if len(rs) == m:
        print(' '.join(map(str, rs)))
        return

    for i in range(num, n+1):
        rs.append(i)
        dfs(i)
        rs.pop()

dfs(1)