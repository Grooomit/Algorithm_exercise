'''
1. 아이디어
- 큐에 첫번째 리스트 0, 1번인덱스 값 추가
- 큐에서 나온 수를 바탕으로 리스트를 for 문으로 돌면서 연결되어 있으면 큐에 추가
- 방문여부 체크해서 아니면 카운트 +1

2. 시간복잡도
- O(V+E) : 1000 + 1000 = 2000

3. 자료구조
- 방문여부 visited : bool[]
- 개수 cnt : int
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)
cnt = 0

def bfs(x):
    global cnt, visited
    q = []
    q.append(x)
    visited[x] = True

    while q:
        node = q.pop()
        
        for i in graph[node]:
            if visited[i]:
                continue
            visited[i] = True
            q.append(i)
    
    cnt += 1

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)

print(cnt)