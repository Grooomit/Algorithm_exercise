# 아이디어 : for 문으로 list로 돌고 해당하는 컴퓨터를 queue에 담는다. 
#           if visited[num]==False: 
#               visited[num] = True
#               cnt += 1

# 시간복잡도 : BFS (V+E) = 100+99 = 199

# 자료구조 : map = int[], 
#           cnt = int, 
#           visited = boolean[]

import sys
input = sys.stdin.readline

visited = [False]*(int(input())+1)

m = int(input())
map = [list(map(int, input().split())) for _ in range(m)]

def bfs(num):
    q = [num]
    cnt = 0
    visited[1] = True
    while len(q) >= 1:
        a = q.pop()
        for i in map:
            if a == i[0] and visited[i[1]] == False:
                visited[i[1]] = True
                cnt += 1
                q.append(i[1])
            elif a == i[1] and visited[i[0]] == False:
                visited[i[0]] = True
                cnt += 1
                q.append(i[0])

    return cnt

print(bfs(1))