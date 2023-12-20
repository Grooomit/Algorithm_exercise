def solution(places):
    answer = []
    for place in places:
        result = False
        for j in range(5):
            for i in range(5):
                if place[j][i] == "P" and not result:                    
                    result = dfs(j, i, 0, place)
        if result:
            answer.append(0)
        else:
            answer.append(1)
    return answer

def dfs(y, x, n, place):
    arr = [(y, x, n, place)]
    dy = (0, -1, 0, 1)
    dx = (1, 0, -1, 0)
    while arr:
        ny, nx, n, place = arr.pop()
        if n >= 2:
            continue
        
        for k in range(4):
            ey = ny + dy[k]
            ex = nx + dx[k]
            
            if 0<=ey<5 and 0<=ex<5:
                if n<2 and place[ey][ex] == "P" and (ey != y and ex != x):
                    return True
                elif place[ey][ex] == "O":
                    arr.append((ey, ex, n+1, place))
    return False