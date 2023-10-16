'''
1. 아이디어
- 각 함수의 교점을 구한다.
- 정수인 교점을 추출한다.
- 각 교점을 나타낼 최소 사이즈를 계산한다.
    - 교점 중 값이 제일 작은 x, y 값을 찾는다. (min(x값), min(y값))
    - 최소 사각형의 사이즈를 계산한다. (max(x값), max(y값))
- 해당 평면에 교점을 *로 나타낸다.

2. 시간복잡도
- 이중 for문 : O(N^2)

3. 자료구조
- 교점리스트 cross: int[][]
- 최소사이즈 x, y: int
'''
def solution(line):
    INF = float('inf')
    cross = []
    x_min, y_min = INF, INF
    x_max, y_max = -INF, -INF
    
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            x, y, not_cross = cross_check(a, b, e, c, d, f)

            if not_cross:
                continue
                
            if x % 1 == 0 and y % 1 == 0:
                x, y = int(x), int(y)
                cross.append((x, y))
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)

    size_x = x_max - x_min + 1
    size_y = y_max - y_min + 1
    answer = [['.' for _ in range(size_x)] for _ in range(size_y)]
    
    for x, y in cross:
        answer[y_max - y][x - x_min] = '*'
            
    result = [''.join(li) for li in answer]
    return result

def cross_check(a, b, e, c, d, f):
    if (a*d - b*c) == 0:
        return 0, 0, True
    
    x = (b*f - e*d) / (a*d - b*c)
    y = (e*c - a*f) / (a*d - b*c)
    
    return x, y, False