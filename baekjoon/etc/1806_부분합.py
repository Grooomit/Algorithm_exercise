'''
1. 아이디어
- while 문으로 부분합 계산
  - if sum(nums[start:end]) >= S 이면, min(end-start, min_cnt) 로 비교
    - start -= 1, 
  - elif end == N 이면, break (마지막 인덱스까지 순회 + 부분합이 S보다 작으므로)
  - else end += 1
- return min_cnt

2. 시간복잡도
- while 문 : O(N)

3. 자료구조
- 최소길이 min_length: int
- 인덱스 start, end: int
- 부분합 sum_num: int
'''

import sys
input = sys.stdin.readline

def solution():
    
    INF = float('inf')
    min_length = INF
    sum_num = nums[0]
    
    start = 0
    end = 1

    while start < N:
        if sum_num >= S:
            min_length = min(min_length, end - start)
            sum_num -= nums[start]
            start += 1
        elif end == N:
            break
        else:
            sum_num += nums[end]
            end += 1
    
    return 0 if min_length == INF else min_length

N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(solution())