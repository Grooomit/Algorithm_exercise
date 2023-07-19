"""
1. 아이디어
- 벽돌의 높이가 주어졌을 때, (외각 벽 2개의 최소값 - 내부벽의 높이) * 내부벽의 갯수
- start, end 변수 선언
- for 문으로 벽돌 순회
  - if block[end] >= block[start] 이면,
    - start 와 end 의 최솟값 * (end - start) - 내부벽의 총 높이 계산
    - start = end
    - end ++

2. 시간복잡도
- for 문 : O(N)

3. 자료구조
- start, end : int
- 구간 벽돌합 sum_block : int
- 전체 빗물 총량 result : int
"""

import sys
input = sys.stdin.readline

def solution(blocks):
    result = 0
    start, end = 0, len(blocks) - 1
    max_left, max_right = blocks[start], blocks[end]

    while start < end:
        max_left, max_right = max(blocks[start], max_left), max(blocks[end], max_right)

        if max_left <= max_right:
            result += max_left - blocks[start]
            start += 1
        else:
            result += max_right - blocks[end]
            end -= 1

    return result

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
print(solution(blocks))