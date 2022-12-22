"""
1. 아이디어
- 백트래킹 재귀함수 안에서 for 로 돌면서 숫자 선택(방문여부 확인)
- 재귀함수에서 숫자가 M 과 같으면, 계산결과를 max 와 비교 return
- 연산자 배열 [+, -, x, /]

2. 시간복잡도
- N! > 가능

3. 자료구조
- 숫자 int[]
- 방문여부 확인 bool[]
- 계산합 int
  
"""

import sys
input = sys.stdin.readline

def dfs(index, total, add, sub, mul, div):
    global maxs, mins
    if index == N:
        maxs = max(maxs, total)
        mins = min(mins, total)
        return

    if add > 0:
        dfs(index+1, total + arr[index], add-1, sub, mul, div)
    if sub > 0:
        dfs(index+1, total - arr[index], add, sub-1, mul, div)
    if mul > 0:
        dfs(index+1, total * arr[index], add, sub, mul-1, div)
    if div > 0:
        if total < 0:
            dfs(index+1, -(abs(total) // arr[index]), add, sub, mul, div-1)
        else: 
            dfs(index+1, total // arr[index], add, sub, mul, div-1)

N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxs = -1e9
mins = 1e9

dfs(1, arr[0], add, sub, mul, div)
print(maxs)
print(mins)