'''
1. 아이디어
- 이중 for 문으로 전체 치킨집의 좌표와 집의 좌표를 각각 리스트에 저장
- 치킨집 중 M개를 뽑는다 (백트래킹 - 조합)
- M개의 치킨집으로 각 집과의 치킨거리를 계산
- 반환된 치킨거리와 기존 최소값 비교
- 치킨집 리스트 전체 반복
- 가장 작은 치킨거리 반환

2. 시간복잡도
- 백트래킹

3. 자료구조
- 도시 city : int[][]
- 치킨집 리스트 store : int[]
- 최소 치킨거리 result : int
- BFS 큐 q : deque
'''

from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
store, houses = [], []
result = 99999

for i in range(N):
    for j in range(N):
        if city[j][i] == 2:
            store.append((j, i))
        if city[j][i] == 1:
            houses.append((j, i))

# 치킨집 M개 선택
def backtracking(chicken, num):
    global result
    if len(chicken) == M:
        result = min(result, calScore(chicken))
        return
    
    for i in range(num, len(store)):
        chicken.append(store[i])
        backtracking(chicken, i+1)
        chicken.pop()

# 도시의 치킨거리 계산
def calScore(chickens):
    score = 0
    for house in houses:
        length = 999
        house_x, house_y = house

        for chicken in chickens:
            chicken_x, chicken_y = chicken
            length = min(length, abs(house_x-chicken_x) + abs(house_y-chicken_y))

        score += length

    return score

backtracking([], 0)
print(result)