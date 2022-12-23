"""
1. 아이디어
- 1~N까지 자연수, 길이 M, 같은수 중복가능
- 백트래킹 재귀함수에서 for 문으로 숫자 선택
- 숫자가 M 이면 return

2. 시간복잡도
- N! = 7*7 < N=8 (가능)

3. 자료구조
- rs = int[]

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []

def dfs(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return

    for i in range(1, n+1):
        rs.append(i)
        dfs(num+1)

        rs.pop()

dfs(0)