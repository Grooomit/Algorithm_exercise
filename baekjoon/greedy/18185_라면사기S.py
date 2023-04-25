'''
1. 아이디어
- 0번 인덱스부터 for 문으로 조회
- 현재 인덱스가 0보다 클 때
    - if N+1 > N+2 일때 2개다사고 3개구매
    - else 3개 다사고 2개구매
    - 나머지 1개씩 전부 구매
- 금액 출력
    
2. 시간복잡도
- *while : O(N) = O(10^4)
- *while-if 문 : O(10^4)
=> O(10^8)

3. 자료구조
- 현재 위치 index : int
- 최소 금액 won : int
'''

import sys
input = sys.stdin.readline

N = int(input())
factory = list(map(int, input().split())) + [0, 0]
won = 0

for i in range(len(factory)-2):

    if factory[i+2] < factory[i+1]:
        minimum = min(factory[i], factory[i+1] - factory[i+2])
        won += 5*minimum
        factory[i] -= minimum
        factory[i+1] -= minimum

        minimum = min(factory[i], factory[i+1], factory[i+2])
        won += 7*minimum
        factory[i] -= minimum
        factory[i+1] -= minimum
        factory[i+2] -= minimum

    else:
        minimum = min(factory[i], factory[i+1], factory[i+2])
        won += 7*minimum
        factory[i] -= minimum
        factory[i+1] -= minimum
        factory[i+2] -= minimum

        minimum = min(factory[i], factory[i+1])
        won += 5*minimum
        factory[i] -= minimum
        factory[i+1] -= minimum
    
    won += 3*factory[i]
    factory[i] = 0

print(won)
