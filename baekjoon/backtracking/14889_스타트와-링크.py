'''
1. 아이디어
- N개 팀에서 N/2 명을 뽑는다. (N은 짝수)
    - 뽑을 때 절반이 넘어가면 중복이 발생하므로, 맨앞자리 한명은 고정
- 팀을 구성한 N/2 명을 제외하고, 남은 선수들을 리스트에 담는다. (조합 - 순서 상관X)
- 구성된 팀 중 같은팀에서 2명씩 뽑는다. (순열 - 순서에 따라 시너지 점수가 달라짐)
- 두 선수의 시너지를 팀 점수에 더해준다.
- 두 팀 모두 수행한다. -> 두 팀의 총 점수 계산
- 두 팀의 총 점수 차가 result 보다 더 작다면 result 값 변경
- 모든 경우의 수를 계산해서 result 최소값 출력

2. 시간복잡도
- 백트래킹 - N^3

3. 자료구조
- 두 팀 리스트 a_team, b_team : list()
- 두 팀 점수 a_score, b_score : int, int
- 두 팀의 최소 점수차 result : int
'''
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
result = 99999

def recur(team):
    global result
    if len(team) == N//2:
        result = min(result, calScore(team))
        return
    
    for i in range(team[-1]+1, N+1):
        team.append(i)
        recur(team)

        team.pop()


def calScore(a_team):
    b_team = [x for x in range(1,N+1) if x not in a_team]
    a_comb_list = list(combinations(a_team, 2))
    b_comb_list = list(combinations(b_team, 2))
    a_score, b_score = 0, 0

    for i in range(len(a_comb_list)):
        a_1, a_2 = a_comb_list[i]
        b_1, b_2 = b_comb_list[i]
        a_score += score[a_1-1][a_2-1] + score[a_2-1][a_1-1]
        b_score += score[b_1-1][b_2-1] + score[b_2-1][b_1-1]

    return abs(a_score - b_score)

recur([1])
print(result)