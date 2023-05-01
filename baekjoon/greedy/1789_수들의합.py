import sys
input = sys.stdin.readline

S = int(input())
result = 0

for i in range(1, S+1):
    result += i

    if S - result <= i:
        print(i)
        break