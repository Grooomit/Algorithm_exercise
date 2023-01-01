"""
1. 아이디어
- 각 사람들이 돈을 뽑는데 걸리는 시간을 cnt 에 합친다.
- 돈을 빨리뽑는 순으로 오름차순 정렬 후 시간 계산

2. 시간복잡도
- for : O(N)

3. 자료구조
- 돈을 뽑는 시간 : int[]
- 총 시간 cnt : int
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
result = 0
nums.sort()

for each_num in nums:
    cnt += each_num
    result += cnt

print(result)