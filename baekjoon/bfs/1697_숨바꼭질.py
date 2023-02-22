'''
1. 아이디어
- bfs 로 방문여부를 체크하면서 deque() 에 이동할 좌표와 시간을 담는다.

2. 시간복잡도
- O(log N)

3. 자료구조
- 
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def s(a, b):
    if a >= b: 
        return a - b
    if a == 0 and b == 1: 
        return 1
    if b % 2: 
        return min(s(a, b - 1), s(a, b + 1)) + 1
    else: 
        return min(b - a, s(a, b // 2) + 1)

print(s(N, K))