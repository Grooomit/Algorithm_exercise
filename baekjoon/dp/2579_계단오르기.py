'''
1. 아이디어
- 계단 오르기 게임. f(x) = 계단을 밟아서 최대점수를 획득하는 함수
- 조건 : 연속 3개를 모두 밟을 수 없다. 마지막 계단은 반드시 밟는다.
    f(1) = 10
    f(2) = 10+20
    f(3) = 10+15 or 10+20+15(=45)
    f(4) = 10+20+25(=55) or 10+15+25
    f(5) = 10+20+25 or 10+20+15

2. 시간복잡도

3. 자료구조
'''

import sys
input = sys.stdin.readline

N = int(input())
step, score = [0]*300, [0]*300

for i in range(N):
    step[i] = int(input())

def step_score(n):
    score = [0]*300
    score[0] = step[0]
    score[1] = step[0]+step[1]
    score[2] = max(step[0], step[1]) + step[2]

    for i in range(3, n):
        score[i] = max(score[i-2], score[i-3]+step[i-1]) + step[i]

    return score[n-1]

print(step_score(N))