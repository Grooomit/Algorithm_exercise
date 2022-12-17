# 아이디어 : dict 에 연결된 정점을 리스트로 저장 -> bfs, dfs 를 이용하여 리스트에 저장
# 시간복잡도 : O(V+E) *2 = (10000 + 1000) *2 = 22000
# 자료구조 : dic = dictionary, bfs,dfs = int[]

from collections import deque

import sys
input = sys.stdin.readline

def dfs(num):
    visited[num] = True
    dfs_list.append(num)

    for i in graph[num]:
        if not visited[i]:
            dfs(i)

def bfs(num):
    visited[num] = True
    q = deque()
    q.append(num)

    while q:
        x = q.popleft()
        bfs_list.append(x)
  
        for j in graph[x]:
            if not visited[j]:
                visited[j] = True
                q.append(j)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

dfs_list, bfs_list = [], []

dfs(start)
visited = [False]*(n+1)
bfs(start)

print(*dfs_list)
print(*bfs_list)