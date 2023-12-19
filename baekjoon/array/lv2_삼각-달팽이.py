'''
1. 아이디어
- 이중 배열을 만든다. [[0]*n for n in range(N)]
- 달팽이 채우기는 패턴이 3가지다.
    - 패턴 1. x축은 고정, y축을 +1 씩 증가하면서 채우기
    - 패턴 2. x축을 +1 씩 증가, y축 고정하고 채우기
    - 패턴 3. x축과 y축을 -1씩 감소하면서 채우기
    
2. 시간복잡도
- 이중 for문 : O(N*N+1/2)

3. 자료구조
- x, y 배열 좌표 : int
- z 달팽이 채우기 패턴 : int
- arr 삼각형 배열 : int[][]
'''

def solution(n):
    answer = []
    arr = [[0]*i for i in range(1, n+1)]
    y, x, z = 0, -1, 0
    num = 1
    for i in range(n, 0, -1):
        for j in range(i):
            if z%3 == 0:
                x += 1
            elif z%3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            arr[x][y] = num
            num += 1
        z += 1
        
    for li in arr:
        for i in li:
            answer.append(i)
    return answer