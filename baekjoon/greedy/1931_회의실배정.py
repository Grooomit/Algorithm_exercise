"""
1. 아이디어
- "1.끝난 시간이 빠른순으로 + 2.시작 시간이 빠른순" 으로 정렬한다.
- for 문으로 돌면서 (회의 끝난시간 < 다음 회의 시작시간) 이 참이면 cnt +1, 회의 진행

2. 시간복잡도
- for : O(N)

3. 자료구조
- 회의 리스트 meeting : int[][]
- 회의 진행수 cnt : int
"""

import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
time = 0
meetings.sort(key=lambda hour: (hour[1], hour[0]))

for each_meeting in meetings:
    if time <= each_meeting[0]:
        cnt += 1
        time = each_meeting[1]

print(cnt)