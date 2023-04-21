'''
1. 아이디어
- 백트래킹으로 1 ~ N 개까지 숫자를 중복없이 순서상관없이 뽑는다.
- 뽑은 숫자들의 합이 S 이면 cnt+1
- 총 cnt 출력

2. 시간복잡도
(1 ≤ N ≤ 20, |S| ≤ 1,000,000)
- 백트래킹: 20C10 = 184756

3. 자료구조
- 뽑은 숫자 choose: int[]
- 횟수 cnt: int
'''

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

def backtracking(choose, chooseSum, num):
    global cnt
    if chooseSum == S and len(choose) > 0:
        cnt += 1

    for i in range(num, len(nums)):
        choose.append(nums[i])
        chooseSum += nums[i]
        backtracking(choose, chooseSum, i+1)
        choose.pop()
        chooseSum -= nums[i]

backtracking([], 0, 0)
print(cnt)

# 하나는 O(1) // not list[k]
# 하나는 최악은 O(N)이지만 평균은 O(1) // 평균이 1이라 흠 그게 힌트? 평균이 O(1) 이라
# 최악 O(N), 평균/최선 O(1) Set, Map 평균/최선은 O(1)이지만 해시충돌이 N개 다 나면 O(N) 네
# 튜플은 해시가 작동하는데 리스트는 안됩니다 그래서 Set에 리스트 못넣음(예외 터짐)