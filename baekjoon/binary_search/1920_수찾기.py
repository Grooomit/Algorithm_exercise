"""
1. 아이디어
- N 개의 수 정렬
- M 개의 수를 이진 탐색
- 이진탐색 후 일치하는 수가 존재하면 return 1 아니면 return 0

2. 시간복잡도
- N 개의 수 정렬 : O(N*log N)
- M 개의 수 이진 탐색 : O(M * log N)
=> 총합 : O((N*M)*log N) 가능

3. 자료구조
- N 개의 수 : int[]
- 탐색할 M 개의 수 : int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort() # 수 정렬

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    
    mid = (st + en) // 2
    if nums[mid] < target:
        search(mid+1, en, target)
    else:
        search(st, mid, target)

for each_target in target_list:
    search(0, N-1, each_target)