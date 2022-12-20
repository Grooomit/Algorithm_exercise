"""
1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택 (방문 여부 확인)
- 재귀함수 안에서 M개를 선택할 경우 return

2. 시간복잡도
- N! > 가능 (N<=8)

3. 자료구조
- 방문여부 bool[][]
- 결과값 지정 int[]

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = [False] * (n+1)
rs = []

def recur(num, a):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(a, n+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            recur(num+1, i)

            check[i] = False
            rs.pop()

recur(0,1)