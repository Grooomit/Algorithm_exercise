import sys
input = sys.stdin.readline

N = int(input())
lopes = [int(input()) for _ in range(N)]
result = 0

lopes.sort(reverse=True)
for i in range(1, N+1):
    if lopes[i-1] * i < result:
        continue

    result = lopes[i-1] * i

print(result)