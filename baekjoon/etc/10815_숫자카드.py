'''
1. 아이디어
- M개의 숫자 카드가 주어졌을 때, 숫자가 내 카드에 포함되는지 결과를 출력

- set 함수를 이용하여 해당 숫자가 집합에 존재하는지 확인
    - 존재하면 1
    - 존재하지않으면 0 을 출력

2. 시간복잡도
- for 문 : O(N) = -10,000,000 ~ 10,000,000 = 20,000,000
- set 은 해시탐색으로 O(1)

3. 자료구조
- 내 카드 mycard: set(int)
- 주어진 카드 리스트 card: int[]
'''

import sys

input = sys.stdin.readline

N = int(input())
mycard = set(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))
result = []

for i in card:
    if i in mycard:
        result.append(1)
    else:
        result.append(0)

print(*result, sep=" ")