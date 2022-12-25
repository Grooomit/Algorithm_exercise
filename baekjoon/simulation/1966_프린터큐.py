"""
1. 아이디어
- 궁금한 문서의 인덱스 index 저장
- 특정 조건(궁금한 문서가 인쇄될때 까지) 전 까지 무한반복 : while
- for 문으로 Queue 문서 확인 -> 나머지 중요도가 모두 낮거나 같으면 인쇄(index-1)
- 중요도가 높은 문서가 존재하면 현재문서를 Queue 맨뒤로 이동(index = len(docs)-1)

2. 시간복잡도
- while : O(V*M) = 100*100 = 10000 < 2억 (가능)

3. 자료구조
- 문서 index : int
- 인쇄 queue : deque()
- 인쇄 횟수 : int
"""
from collections import deque

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = deque()
    q.extend(list(map(int, input().split())))
    cnt = 1

    while 1:
        printing = True
        for i in range(len(q)):
            if q[0] < q[i]:
                q.append(q.popleft())
                M -= 1
                if M < 0:
                    M += len(q)
                printing = False
                break
        
        if printing == True:
            if M == 0:
                break
            else:
                cnt += 1
                q.popleft()
                M -= 1
    
    print(cnt)