"""
1. 아이디어
- 백트래킹 재귀함수 for 문으로 숫자 선택 (이때 if 방문여부 확인)
- 재귀함수에서 M 개를 선택한 경우 return

2. 시간복잡도
- 중복 미허용 N! > 가능 / N <= 15, 시간 10초

3. 자료구조
- 방문 여부 확인 bool[][]
- 경우의수 int

"""

import sys
input = sys.stdin.readline

# def check(num):
#     for i in range(num):
#         if board[num] == board[i] or abs(board[num] - board[i]) == abs(num - i):
#             return False
#     return True

def recur(num):
    global cnt
    if num == n:
        cnt += 1
        return
    
    for i in range(n):
        # x축, +대각선, -대각선에 퀸이 존재하는지 확인
        if (not a[i] and not b[num+i] and not c[num-i+n-1]) :
            a[i] = b[num+i] = c[num-i+n-1] = True
            recur(num+1)
            a[i] = b[num+i] = c[num-i+n-1] = False

cnt = 0
n = int(input())
# x축, +대각선, -대각선
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

recur(0)
print(cnt)